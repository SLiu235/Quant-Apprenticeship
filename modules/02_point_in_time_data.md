# Module 02 — Point-in-time data and feature pipeline

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/02_point_in_time_data.md) · [Optional assessment](../assessments/integrated/02_point_in_time_data.md)

## Objective

Reconstruct the information set available at a historical decision and preserve that view after later corrections.

## Prerequisites and pace

Module 1: contracts, reproducible runs and explicit timestamps. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Event time answers when something happened. Publication time answers when it was released. Receipt/availability time answers when this system could use it. A version identifies a correction. The eligibility rule is event_at ≤ cutoff and available_at ≤ cutoff; among eligible revisions of an event, choose the latest received revision with an explicit tie rule. Do not infer actual vendor latency from a publication timestamp. Schema and key validation must precede joins. A current universe also does not establish historical investability.

## Mental models

Data is a sequence of claims that became available over time. A historical query asks what the system knew then, not what the database says now. Preserve raw revisions and keep decision-time feature snapshots immutable.

## Worked example

A value of 100 concerns Monday and arrives Monday 17:05. A correction to 103 arrives Wednesday 12:00. Tuesday decisions must still see 100. Thursday decisions may use 103. A join on event date without availability time silently changes the historical experiment.

## Implementation

Inspect the fixture and implement an independent as-of selector. Materialize features with source event, receipt time and version. Add a SQL implementation using a partitioned row-number query over eligible revisions and compare it with the Python selector.

Read the contracts and trace one observation before editing. Reference code: [data.py](../apprentice_system/data.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 2 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Joining only on ticker/date; treating a date as a timezone-aware instant; adjusted prices mixed with unadjusted execution; duplicate revisions; silent missing-symbol drops; current membership applied retrospectively.

## Debugging exercise

Inject a revision received after the decision and inspect the earliest changed feature. Assert that earlier decisions remain byte-identical. Inject a duplicate key and a timezone-naive timestamp; determine where they should be rejected.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose JSON, Parquet with DuckDB, or PostgreSQL for immutable daily snapshots used by one researcher. Decide first. Include concurrent writers, transactional requirements, expected scan size and recovery in the comparison.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

An auditable as-of join; duplicate and schema checks; a future-revision invariance test; explicit missing-data and universe policies; lineage for one feature.

## Deeper teaching and existing worked projects

[02 availability](../lessons/02_availability.md) · [06 sessions](../lessons/06_sessions.md) · [07 data pipeline](../lessons/07_data_pipeline.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/01_edge_and_data.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
