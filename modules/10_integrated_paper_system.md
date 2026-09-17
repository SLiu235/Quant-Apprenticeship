# Module 10 — Integrated paper portfolio and investment committee

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/10_integrated_paper_system.md) · [Optional assessment](../assessments/integrated/10_integrated_paper_system.md)

## Objective

Own a complete simulation run, defend its investment interpretation and explain what evidence is still missing.

## Prerequisites and pace

Modules 1–9 with understood limitations; milestone verification before relying on integrated state. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Integration exposes mismatched assumptions: a forecast may target intraday returns while carried inventory earns overnight P&L; a model may be frozen while feature definitions change; target constraints may not hold after partial fills. Reconcile these contracts explicitly. Preserve a record of every forecast, target, order, fill and mark. Compare feasible baselines under identical execution and accounting rules. A synthetic integration test demonstrates behavior of the software under stipulated conditions, not market profitability or production readiness.

## Mental models

The owner is accountable for the entire decision chain. A correct component is insufficient if interfaces disagree about clocks, units or responsibilities. The strongest committee memo may recommend rejecting the strategy or collecting a better dataset.

## Worked example

The reference forecasts midpoint-to-close return but carries holdings between sessions. Its total P&L therefore includes overnight exposure outside the forecast target. It also marks final inventory without liquidating it. Both are explicit limitations; claiming total P&L validates the intraday forecast would be wrong.

## Implementation

Run all ten stages and reconstruct the final book from persisted fills. Produce a committee memo separating numerical correctness, research validity, economic significance and operational readiness. Implement and compare either explicit end-of-session liquidation or a forecast/holding horizon that matches carried inventory.

Read the contracts and trace one observation before editing. Reference code: [run.py](../apprentice_system/run.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 10 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Attributing all portfolio P&L to the signal; terminal inventory without cost disclosure; different costs across baselines; ignoring open orders on restart; fabricated confidence; presenting a toy simulator as a broker integration.

## Debugging exercise

Inject a mismatch between forecast version and portfolio run, a duplicate fill and a stale mark. Trace the earliest violated contract. Reconstruct expected balances from the immutable evidence and explain whether recovery changes the investment conclusion.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Act as the investment committee: reject, continue research, or authorize a tightly scoped prospective paper study. State the strongest opposing argument, the information that would change your vote and the conditions for stopping.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

One-command replay; reconciled event history; matched baselines; horizon-consistent accounting or an explicit attribution split; stress/cost sensitivity; incident recovery evidence; committee memo and an honest skills-gap update. No automatic promotion or capital deployment.

## Deeper teaching and existing worked projects

[21 operations](../lessons/21_operations.md) · [22 capstone protocol](../lessons/22_capstone_protocol.md) · [23 replication review](../lessons/23_replication_review.md) · [24 research career](../lessons/24_research_career.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/06_research_ownership.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
