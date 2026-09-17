# Module 06 — Transaction costs and execution simulation

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/06_execution_microstructure.md) · [Optional assessment](../assessments/integrated/06_execution_microstructure.md)

## Objective

Evaluate the complete execution mandate, including partial fills, adverse selection and the cost of not trading.

## Prerequisites and pace

Modules 2, 4 and 5; decision clocks, orders and reconciled accounting. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Arrival shortfall on signed fills is Σq_f(p_f−p_arrival)+fees. Decision shortfall uses the earlier decision price; the difference exposes delay. Unfilled opportunity cost requires a stated terminal benchmark and a frozen mandate. The reference stipulates half-spread plus k√participation as slippage; this is a teaching assumption, not calibrated impact or an exchange rule. Realized interval volume belongs to the fill simulator; a scheduler cannot know it in advance. Passive fills require queue assumptions and can select precisely the paths on which trading is unattractive.

## Mental models

Signal, target portfolio, orders and fills are separate objects. Assess the entire original order, not just its cheapest fills. More urgency raises immediate execution cost; less urgency can increase price risk and missed-opportunity cost. The right balance depends on signal decay and the mandate.

## Worked example

Buy 100 shares with an arrival midpoint of $100. Only 50 fill at $100.05, with $0.01 per-share fee. Executed shortfall is $3. If the unfilled 50 are valued at a $101 terminal benchmark, opportunity cost is $50. Reporting only the executed price hides most of the mandate shortfall.

## Implementation

Run the partial IOC model, TWAP quantity schedule and the existing passive FIFO reference. Extend the event reducer with cancel requests, acknowledgments and late fills. Add spread/impact/participation sensitivity and a TCA report that freezes benchmark definitions.

Read the contracts and trace one observation before editing. Reference code: [execution.py](../apprentice_system/execution.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 6 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Assuming a touched limit fills; using future volume for scheduling; treating a cancel request as final; forgetting sell signs; duplicate fill application; ignoring unfilled quantities; choosing VWAP after seeing which benchmark flatters performance.

## Debugging exercise

Reproduce a partial fill followed by cancel request, another fill and cancel acknowledgment. After every event require original quantity = filled + cancelled + live remainder, using consistent side conventions. Inject a duplicate fill and a sequence gap.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

A short-lived signal competes with a wide spread and thin depth. Choose immediate execution, passive posting, a staged schedule or no trade. State the assumptions about signal decay, queue position and adverse selection that drive your choice.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Order conservation; buy/sell cost checks; explicit fill assumptions; delay/spread/impact/fees/opportunity decomposition; cost sensitivity; queue and cancel-race tests; a no-trade case.

## Deeper teaching and existing worked projects

[04 instruments](../lessons/04_instruments.md) · [05 execution](../lessons/05_execution.md) · [06 sessions](../lessons/06_sessions.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/04_economic_value.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
