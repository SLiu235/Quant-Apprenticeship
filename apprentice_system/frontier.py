"""Research controls and economic comparisons for the professional track."""

import argparse
from pathlib import Path
from statistics import mean
from .core import encoded, fingerprint, source_hashes
from .data import fixture
from .research import walk_forward
from .research_control import ExperimentBook
from .validation import paired_date_interval
from .run import paper_replay
from .ai_evaluation import demo as ai_demo


def run(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    data = fixture()
    forecasts = walk_forward(data)
    dates = sorted({f["day"] for f in forecasts})
    split = dates[int(len(dates) * 0.6)]
    outcomes = {
        (r["symbol"], r["event_at"][:10]): r["close"] / r["mid"] - 1
        for r in data["bars"]
    }
    protocol = dict(
        hypothesis="Lagged synthetic information improves squared-error loss over zero",
        primary_metric="equally date-weighted squared error",
        universe="AAA BBB CCC synthetic",
        horizon="16:00 midpoint to 17:00 close",
        data_hash=fingerprint(data),
        split=dict(development_end_exclusive=split, evaluation_start=split),
        cost_policy="separate matched-policy/capital/cost grid; no significance selection",
        kill_rule="reject improvement claim if selected loss does not beat zero",
        evaluation_status="synthetic",
        code_hash=fingerprint(source_hashes()),
        procedure="expanding fit with matured prior labels; choices fixed before evaluation",
    )
    study_id = fingerprint(protocol)
    book = ExperimentBook(output / "experiments.sqlite")

    def losses(name, group):
        return [
            dict(
                id=f["day"] + ":" + f["symbol"],
                date=f["day"],
                loss=(
                    outcomes[(f["symbol"], f["day"])]
                    - (
                        f["alpha"]
                        if name == "linear"
                        else f["x"]
                        if name == "persistence"
                        else 0
                    )
                )
                ** 2,
            )
            for f in group
        ]

    try:
        book.register(study_id, protocol, budget=3)
        development = [f for f in forecasts if f["day"] < split]
        scores = {}
        for name in ("zero", "persistence", "linear"):
            book.reserve(
                study_id,
                name,
                dict(
                    family=name, feature="lagged return", seed=7, schedule="expanding"
                ),
            )
            scores[name] = mean(r["loss"] for r in losses(name, development))
            book.finish(
                study_id, name, dict(status="completed", development_mse=scores[name])
            )
        selected = min(scores, key=lambda name: (scores[name], name))
        book.lock_selection(study_id, selected)
        evaluation = [f for f in forecasts if f["day"] >= split]
        comparison = paired_date_interval(
            losses(selected, evaluation), losses("zero", evaluation), block=3
        )
        book.record_evaluation(
            study_id,
            dict(selected=selected, comparison=comparison, evidence="synthetic"),
        )
        research = book.snapshot(study_id)
    finally:
        book.close()
    economics = []
    for capital in (100000.0, 1000000.0):
        for costs in (0.0, 1.0, 3.0):
            for policy in ("cash", "equal_weight", "signal"):
                replay = paper_replay(
                    data,
                    forecasts,
                    policy=policy,
                    cost_scale=costs,
                    initial_cash=capital,
                )
                requested = sum(abs(e["order"]["quantity"]) for e in replay["events"])
                filled = sum(abs(e["filled"]) for e in replay["events"])
                economics.append(
                    dict(
                        policy=policy,
                        capital=capital,
                        cost_scale=costs,
                        net_return=replay["net_pnl"] / capital,
                        max_drawdown=replay["max_drawdown"],
                        fill_fraction=filled / requested if requested else None,
                        horizon_attribution=replay["horizon_attribution"],
                        final_inventory_marked_dollars=replay["final_equity"]
                        - replay["final_cash"],
                    )
                )
    result = dict(
        research=research,
        economic_comparisons=economics,
        ai_evaluation=ai_demo(),
        scope="synthetic workflow and stress diagnostics; toy capacity; not calibrated liquidity or investability",
        benchmark_note="same constraints/costs/calendar, but different realized exposures; equal weight is a mandate comparator, not risk-matched alpha attribution",
    )
    (output / "frontier_report.json").write_bytes(encoded(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("outputs/frontier"))
    args = parser.parse_args()
    result = run(args.output)
    print(
        f"Research protocol locked; {len(result['economic_comparisons'])} matched policy/cost/capital scenarios. Report: {args.output.resolve() / 'frontier_report.json'}"
    )


if __name__ == "__main__":
    main()
