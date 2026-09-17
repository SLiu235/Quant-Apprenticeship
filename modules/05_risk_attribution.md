# Module 05 — Risk, scenarios and P&L attribution

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/05_risk_attribution.md) · [Optional assessment](../assessments/integrated/05_risk_attribution.md)

## Objective

Explain portfolio losses in dollars, distinguish exposures from scenarios, and reconcile P&L independently.

## Prerequisites and pace

Module 4: holdings, target weights, cash and exposure limits. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

For initial inventory q₀, prior marks p₀, final marks p₁ and signed fills Δq at execution prices p_f, P&L = Σq₀(p₁−p₀) + ΣΔq(p₁−p_f) − fees, assuming no other cashflows. Dividends, borrow and financing require separate ledger entries. This accounting identity is different from factor attribution. A factor model separates common exposures from residual behavior under model assumptions; a stress scenario asks what happens under a specified shock without claiming its probability.

## Mental models

The first risk report is a correct book of positions and cash. Reconcile before interpreting. A scenario is useful when its mechanism is explicit, including what becomes illiquid or correlated; a decorative severe number is less useful.

## Worked example

Start with two shares marked at $100. Buy three at $101 and pay $1 fee. Mark all shares at $102. Carry P&L is $4; trade-to-mark P&L is $3; fees are $1; net P&L is $6. Independently compute the change in cash plus marked inventory.

## Implementation

Use the reference attribution identity and named price shocks. Add independent balance-sheet reconciliation. Then introduce an explicit factor exposure report with an estimation window and stress the residual assumptions.

Read the contracts and trace one observation before editing. Reference code: [risk.py](../apprentice_system/risk.py) · [execution.py](../apprentice_system/execution.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 5 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Fees deducted twice; dividends missing; stale marks; short-sale proceeds treated as profit; factor residual mistaken for pure skill; zero scenario return caused by missing symbol mapping; normal-period covariance used as a crisis guarantee.

## Debugging exercise

Create a one-dollar discrepancy and test cash entries, quantities, mark timestamps and price units. Find the first event where ledger equity and independently explained P&L diverge. Do not plug the residual into an unexplained bucket.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

A strategy has small historical volatility but concentrated exposure to one funding mechanism. Decide whether to lower size, add a hedge, tighten liquidity limits or gather more evidence. State how you would detect hedge failure.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Reconciled daily P&L; explicit costs/cashflows; exposure and scenario reports; named residual limitations; one failure postmortem; no unexplained accounting residual.

## Deeper teaching and existing worked projects

[04 instruments](../lessons/04_instruments.md) · [14 risk forecasts](../lessons/14_risk_forecasts.md) · [15 portfolios](../lessons/15_portfolios.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/04_economic_value.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
