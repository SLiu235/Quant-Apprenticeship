# Module 03 — Signal research and validation

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/03_signal_research.md) · [Optional assessment](../assessments/integrated/03_signal_research.md)

## Objective

Evaluate a hypothesis against simple baselines without allowing future labels or model selection to contaminate the result.

## Prerequisites and pace

Module 2: defensible information clocks and features. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Freeze features at each decision. At each training cutoff include only labels already available. Fit preprocessing inside the training window. Expanding and rolling windows express different stability assumptions. Forecast loss, rank information and portfolio P&L answer different questions. For overlapping targets, reason with label intervals and purge training observations that overlap the evaluation horizon; an embargo is an additional separation rule, not a universal cure. Record all variants considered, including unsuccessful ones. A bootstrap must preserve the dependence relevant to the statistic.

## Mental models

A holdout is a budget of unseen evidence. Once a result influences a choice, that result is development evidence. More searches require stronger skepticism, not a higher reported maximum Sharpe ratio.

## Worked example

A Monday decision forecasts Monday-to-Friday return. That target is not fully observed on Tuesday. Placing the Monday row into Tuesday training because its feature timestamp is old leaks the rest of the week. Filter on label availability as well as feature availability.

## Implementation

Run the expanding single-feature regression and compare zero and persistence forecasts on identical rows. Independently reproduce losses. Extend evaluation to paired date-level loss differences with an explicit dependence model. Keep synthetic software checks separate from the existing empirical audit.

Read the contracts and trace one observation before editing. Reference code: [research.py](../apprentice_system/research.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 3 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Global standardization; random panel splits with overlapping outcomes; repeated holdout inspection; dropping missing rows differently by model; interpreting training residual RMSE as calibrated confidence; selecting the best dependence block after seeing significance.

## Debugging exercise

Multiply future prices by three and verify that all preceding forecasts are unchanged. If not, find the earliest changed feature, fitted parameter or label inclusion. Introduce a five-session target and inspect label maturity explicitly.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose a zero/linear baseline or a transformer for a small selected panel. Specify the evidence, data scale and evaluation improvement that would earn the complex model a place.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Frozen hypothesis and variant ledger; matched baseline comparison; chronological split diagram; leakage mutation test; uncertainty interpretation; a negative-result decision as defensible as a positive one.

## Deeper teaching and existing worked projects

[03 scoring](../lessons/03_scoring.md) · [08 baseline](../lessons/08_baseline.md) · [09 validation](../lessons/09_validation.md) · [13 time series ai](../lessons/13_time_series_ai.md) · [23 replication review](../lessons/23_replication_review.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/02_research_discovery.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
