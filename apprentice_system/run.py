"""One CLI, ten cumulative stages, deterministic local-only outputs."""

import argparse
from copy import deepcopy
import json
from pathlib import Path
import platform

from .core import encoded, finite, fingerprint, research_contract, source_hashes
from .data import SYMBOLS, features, fixture, validate_bars
from .research import evaluate, walk_forward
from .portfolio import orders, weights
from .risk import attribution, check_weights, scenarios
from .execution import Ledger, simulate, twap
from .pipeline import EventStore, artifact
from .copilot import evidence_valid, retrieve
from .monitoring import alerts


def paper_replay(
    dataset: dict,
    forecasts: list[dict],
    participation: float = 0.05,
    policy: str = "signal",
    cost_scale: float = 1.0,
    initial_cash: float = 100000.0,
) -> dict:
    if policy not in {"signal", "equal_weight", "cash"}:
        raise ValueError("unknown policy")
    if (
        finite(cost_scale, "cost scale") < 0
        or finite(initial_cash, "initial cash") <= 0
    ):
        raise ValueError("invalid cost/capital")
    if not 0 < finite(participation, "participation") <= 1:
        raise ValueError("invalid participation")
    ledger = Ledger(cash=initial_cash)
    quotes = {(q["symbol"], q["at"][:10]): q for q in dataset["quotes"]}
    if len(quotes) != len(dataset["quotes"]):
        raise ValueError("duplicate quote key")
    daily, events = [], []
    previous_marks = None
    for day in sorted({f["day"] for f in forecasts}):
        fs = [f for f in forecasts if f["day"] == day]
        if len(fs) != len(SYMBOLS) or {f["symbol"] for f in fs} != set(SYMBOLS):
            raise ValueError("missing or duplicate forecast symbol")
        sizing_prices = {f["symbol"]: f["sizing_price"] for f in fs}
        # Research revisions may alter sizing inputs, but cannot rewrite the
        # prior accounting mark or retroactively change reported starting NAV.
        old_marks = previous_marks if previous_marks is not None else sizing_prices
        new_marks = {s: quotes[(s, day)]["close"] for s in SYMBOLS}
        arrival_marks = {s: quotes[(s, day)]["mid"] for s in SYMBOLS}
        # Validate the complete market snapshot, including days with no orders.
        for symbol in SYMBOLS:
            q = quotes[(symbol, day)]
            checks = alerts(day + "T16:00:00+00:00", q["at"], 1, 1, 0, 0)
            if checks or any(finite(q[name], name) <= 0 for name in ("mid", "close")):
                raise ValueError("invalid execution snapshot: " + str(checks))
        old_equity, old_holdings = ledger.equity(old_marks), dict(ledger.holdings)
        target = (
            weights({f["symbol"]: f["alpha"] for f in fs})
            if policy == "signal"
            else {
                s: 0.8 / len(SYMBOLS) if policy == "equal_weight" else 0.0
                for s in SYMBOLS
            }
        )
        check_weights(target)
        intent = orders(target, ledger.holdings, old_equity, sizing_prices, day)
        fills, day_events = [], []
        for order in intent:
            quote = dict(quotes[(order["symbol"], day)])
            quote["spread_bps"] *= cost_scale
            # Simulator alone sees the future execution quote and interval volume.
            result = simulate(
                order,
                quote,
                participation=participation,
                impact_bps=10 * cost_scale,
                fee_per_share=0.005 * cost_scale,
            )
            fill = result["fill"]
            if fill:
                ledger.apply(fill)  # fail closed on infeasible fills
                fills.append(fill)
            events.append(result)
            day_events.append(result)
        equity = ledger.equity(new_marks)
        explained = attribution(old_holdings, old_marks, new_marks, fills)
        overnight = sum(
            qty * (arrival_marks[s] - old_marks[s]) for s, qty in old_holdings.items()
        )
        intraday = sum(
            qty * (new_marks[s] - arrival_marks[s])
            for s, qty in ledger.holdings.items()
        )
        execution_cost = sum(
            f["quantity"] * (f["price"] - arrival_marks[f["symbol"]]) + f["fee"]
            for f in fills
        )
        horizon_pnl = overnight + intraday - execution_cost
        if abs(equity - old_equity - explained["net_pnl"]) > 1e-7:
            raise ValueError("attribution does not reconcile")
        if abs(horizon_pnl - explained["net_pnl"]) > 1e-7:
            raise ValueError("forecast-horizon attribution does not reconcile")
        observed = {
            s: ledger.holdings.get(s, 0) * new_marks[s] / equity for s in SYMBOLS
        }
        warning = alerts(
            day + "T17:00:00+00:00",
            day + "T17:00:00+00:00",
            equity,
            old_equity + explained["net_pnl"],
            sum(observed.values()),
            max(observed.values()),
        )
        if warning:
            raise ValueError(str(warning))
        daily.append(
            dict(
                day=day,
                equity=equity,
                cash=ledger.cash,
                holdings=dict(ledger.holdings),
                target=target,
                observed_weights=observed,
                attribution=explained,
                horizon_attribution=dict(
                    overnight_pnl=overnight,
                    intraday_market_pnl=intraday,
                    execution_cost=execution_cost,
                    net_pnl=horizon_pnl,
                ),
                reconciliation_residual=equity - old_equity - explained["net_pnl"],
                filled_notional=sum(abs(f["quantity"] * f["price"]) for f in fills),
                arrival_shortfall=sum(
                    e["arrival_shortfall_dollars"] for e in day_events
                ),
            )
        )
        previous_marks = dict(new_marks)
    if not daily:
        raise ValueError("no paper sessions")
    peak, drawdown = initial_cash, 0.0
    for d in daily:
        peak = max(peak, d["equity"])
        drawdown = min(drawdown, d["equity"] / peak - 1)
    return dict(
        data_kind="synthetic paper replay",
        initial_cash=initial_cash,
        policy=policy,
        cost_scale=cost_scale,
        participation=participation,
        final_cash=ledger.cash,
        final_holdings=ledger.holdings,
        final_equity=daily[-1]["equity"],
        max_drawdown=drawdown,
        net_pnl=daily[-1]["equity"] - initial_cash,
        horizon_attribution={
            key: sum(d["horizon_attribution"][key] for d in daily)
            for key in (
                "overnight_pnl",
                "intraday_market_pnl",
                "execution_cost",
                "net_pnl",
            )
        },
        fills=list(ledger.fills.values()),
        events=events,
        daily=daily,
        limitations=[
            "stipulated spread/impact, no calibration",
            "IOC participation cap uses realized interval volume in simulator",
            "no passive queue, short borrow, dividends, financing or exchange calendar",
            "end inventory marked, not liquidated; no terminal liquidation costs",
            "regression horizon is intraday; carried inventory adds overnight exposure",
        ],
    )


def run(stage: int, output: Path, seed: int = 7, participation: float = 0.05) -> dict:
    if not 1 <= stage <= 10:
        raise ValueError("stage must be 1..10")
    output.mkdir(parents=True, exist_ok=True)
    dataset = fixture(seed)
    config = dict(
        seed=seed,
        participation=participation,
        stages=stage,
        python=platform.python_version(),
        data_hash=fingerprint(dataset),
        sources=source_hashes(),
    )
    run_id = fingerprint(config)
    reports = {}

    def save(number, value):
        reports[number] = value
        (output / f"stage_{number:02d}.json").write_bytes(encoded(value))

    save(1, dict(contract=research_contract(), run_id=run_id, manifest=config))
    if stage >= 2:
        validate_bars(dataset["bars"])
        cutoff = dataset["days"][2] + "T15:55:00+00:00"
        save(
            2,
            dict(
                data_kind=dataset["data_kind"],
                rows=len(dataset["bars"]),
                cutoff=cutoff,
                features=features(dataset["bars"], cutoff),
            ),
        )
        (output / "synthetic_fixture.json").write_bytes(encoded(dataset))
    if stage >= 3:
        forecasts = walk_forward(dataset)
        save(3, dict(evaluation=evaluate(forecasts, dataset), forecasts=forecasts))
    if stage >= 4:
        last = [f for f in forecasts if f["day"] == forecasts[-1]["day"]]
        target = weights({f["symbol"]: f["alpha"] for f in last})
        save(
            4,
            dict(
                target=target,
                cash_weight=1 - sum(target.values()),
                orders=orders(
                    target,
                    {},
                    100000,
                    {f["symbol"]: f["sizing_price"] for f in last},
                    "demo",
                ),
            ),
        )
    if stage >= 5:
        check_weights(target)
        shocks = {
            "broad_down_10pct": {s: -0.10 for s in SYMBOLS},
            "AAA_down_30pct": {s: -0.30 if s == "AAA" else 0.0 for s in SYMBOLS},
        }
        save(
            5,
            dict(
                scenario_portfolio_returns=scenarios(target, shocks),
                scope="specified linear price shocks; cash unchanged; not VaR probabilities",
            ),
        )
    if stage >= 6:
        replay = paper_replay(dataset, forecasts, participation)
        save(6, dict(replay=replay, twap_example=twap(103, 4)))
    if stage >= 7:
        artifacts = output / "artifacts"
        data_file = artifact(artifacts, dataset)
        model_file = artifact(
            artifacts, dict(model=forecasts[-1]["model"], manifest=config)
        )
        store = EventStore(output / f"events-{run_id[:16]}.sqlite")
        try:
            for fill in replay["fills"]:
                store.append(fill["fill_id"], fill)
            # Reopening the database makes restart persistence part of the demo.
        finally:
            store.close()
        store = EventStore(output / f"events-{run_id[:16]}.sqlite")
        restarted = Ledger()
        try:
            for fill in store.events():
                restarted.apply(fill)
        finally:
            store.close()
        if (
            abs(restarted.cash - replay["final_cash"]) > 1e-8
            or restarted.holdings != replay["final_holdings"]
        ):
            raise ValueError("restart mismatch")
        save(
            7,
            dict(
                data_artifact=data_file.name,
                model_artifact=model_file.name,
                restart_matches=True,
                persisted_fills=len(replay["fills"]),
                scope="local fill replay and immutable artifacts; no live order recovery or broker reconciliation",
            ),
        )
    if stage >= 8:
        cutoff = "2025-06-01T00:00:00+00:00"
        answer, abstain = (
            retrieve("execution costs", cutoff),
            retrieve("zebra migration", cutoff),
        )
        invented = deepcopy(answer)
        invented["quote"] = "Guaranteed profit."
        save(
            8,
            dict(
                baseline="deterministic lexical retrieval; no model calls",
                answer=answer,
                abstention=abstain,
                evidence_check=evidence_valid(answer, cutoff),
                fabricated_quote_rejected=not evidence_valid(invented, cutoff),
                limits="citation matching does not establish semantic truth or retrieval completeness",
            ),
        )
    if stage >= 9:
        save(
            9,
            dict(
                healthy=alerts(
                    "2025-01-01T16:00:00+00:00",
                    "2025-01-01T16:00:00+00:00",
                    100,
                    100,
                    0.5,
                    0.2,
                ),
                stale=alerts(
                    "2025-01-01T16:05:00+00:00",
                    "2025-01-01T16:00:00+00:00",
                    100,
                    100,
                    0.5,
                    0.2,
                ),
                unreconciled=alerts(
                    "2025-01-01T16:00:00+00:00",
                    "2025-01-01T16:00:00+00:00",
                    99,
                    100,
                    0.5,
                    0.2,
                ),
                runbook="Pause new orders; preserve evidence; reconcile; fix; rerun regression; explicitly authorize resume.",
            ),
        )
    if stage >= 10:
        save(
            10,
            dict(
                run_id=run_id,
                sessions=len(replay["daily"]),
                net_pnl=replay["net_pnl"],
                max_drawdown=replay["max_drawdown"],
                max_accounting_residual=max(
                    abs(d["reconciliation_residual"]) for d in replay["daily"]
                ),
                decision="Do not infer investability from synthetic data. Continue to independently validated empirical research.",
                forecast_evaluation=reports[3]["evaluation"],
                limitations=replay["limitations"],
            ),
        )
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=int, choices=range(1, 11), default=10)
    parser.add_argument("--output", type=Path, default=Path("outputs/integrated"))
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--participation", type=float, default=0.05)
    args = parser.parse_args()
    reports = run(args.stage, args.output, args.seed, args.participation)
    print(
        json.dumps(
            dict(
                stages=list(reports),
                output=str(args.output.resolve()),
                data_kind="synthetic",
                status="completed",
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
