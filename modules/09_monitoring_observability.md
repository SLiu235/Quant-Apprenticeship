# Module 09 — Monitoring, drift and incident response

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/09_monitoring_observability.md) · [Optional assessment](../assessments/integrated/09_monitoring_observability.md)

## Objective

Detect actionable failures, preserve diagnostic evidence and restore operation through explicit checks.

## Prerequisites and pace

Module 7 recovery; Module 8 evidence and model-version boundaries. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Monitor invariants before performance: data freshness, timestamp order, schema identity, model/feature compatibility, order state, cash and P&L reconciliation. Input drift, prediction drift and realized performance deterioration are different signals, often observed at different delays. An alert needs an owner, an action and an escalation path. The reference checks a few deterministic invariants; statistical drift detection and alert routing remain project extensions.

## Mental models

Ask what action would change when an alert fires. A metric without a decision is a chart. During an incident, halt new risk if the state is unreliable, but continue recording and reconciling economically real events.

## Worked example

A feed process is healthy and returns successful HTTP responses, but its quote timestamp is five minutes old. Availability of the process is not freshness of its data. A monotonic sequence and explicit timestamp-age check can detect a failure hidden by status-code monitoring.

## Implementation

Run healthy, stale and unreconciled fixtures. Add model/feature mismatch and delayed labels. Build a replayable incident trace and a small batch report with severity, owner, evidence and response.

Read the contracts and trace one observation before editing. Reference code: [monitoring.py](../apprentice_system/monitoring.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 9 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Healthy process serving stale data; NaN comparisons passing silently; noisy alerts ignored; resuming before reconciliation; monitoring only aggregate P&L; reacting to a normal regime change by blindly retraining.

## Debugging exercise

Begin at the earliest failed invariant, not the last exception. Preserve the offending event, source version and clock. Form competing explanations and identify the smallest observation that distinguishes them.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

A live shadow forecast distribution shifts but input schemas and prices remain valid. Choose halt, reduced risk, human review or continued observation. Specify the evidence that would change your decision; drift alone does not identify a broken model.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Actionable alert catalog; freshness/NaN/reconciliation tests; incident timeline; restart/resume criteria; concise postmortem; clear separation between operational failure and investment underperformance.

## Deeper teaching and existing worked projects

[20 compute](../lessons/20_compute.md) · [21 operations](../lessons/21_operations.md) · [23 replication review](../lessons/23_replication_review.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/06_research_ownership.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
