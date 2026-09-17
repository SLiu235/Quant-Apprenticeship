# Module 07 — Production data and model pipelines

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/07_production_pipelines.md) · [Optional assessment](../assessments/integrated/07_production_pipelines.md)

## Objective

Persist validated artifacts and recover state after retry or restart without silent duplication.

## Prerequisites and pace

A deterministic Modules 1–6 replay with meaningful failure tests. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Content hashes identify exact artifacts; model artifacts must also identify compatible feature schema and training data. Publication should expose complete files, not partly written results. The reference writes and fsyncs a temporary file, then publishes by a no-overwrite link. SQLite stores ordered events with a unique event ID in a transaction. Deduplication plus deterministic replay gives a useful local guarantee; it does not create exactly-once delivery across a network or an exchange.

## Mental models

Design around retry, because failure often happens after work succeeds but before acknowledgment arrives. Separate immutable facts from derived state. A restart should reconstruct what happened, not improvise what probably happened.

## Worked example

A fill is committed to storage and the process crashes before returning success. On retry, the same ID and payload should be accepted as already present. If the payload differs, stop and investigate. A new event ID for the same economic fill would bypass this protection, so the source identity contract matters.

## Implementation

Run artifact hashing, SQLite event persistence and cash/holdings reconstruction. Add explicit model/feature compatibility checks, a batch state record and a rollback pointer. Document recovery for failure before commit, after commit and during publication.

Read the contracts and trace one observation before editing. Reference code: [pipeline.py](../apprentice_system/pipeline.py) · [run.py](../apprentice_system/run.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 7 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Retry with a fresh identifier; using filename as model identity; mutable latest data; corrupted cached output; state updated before the durable event; crash recovery that loses open-order intentions; assuming local durability proves distributed safety.

## Debugging exercise

Terminate a subprocess after committing an event but before acknowledging it, then retry. Compare cash, inventory and event count. Corrupt an artifact and verify that reuse fails visibly. Separate expected duplicates from conflicting duplicates.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose one scheduled process with SQLite/files, a queue plus workers, or distributed services. Give an observed concurrency, latency or reliability requirement for each added component.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Stable IDs; restart reconstruction; corruption detection; model/schema contract; documented failure boundaries and rollback; tests of an actual interrupted subprocess in your extension.

## Deeper teaching and existing worked projects

[19 research software](../lessons/19_research_software.md) · [20 compute](../lessons/20_compute.md) · [21 operations](../lessons/21_operations.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/03_predictive_ai.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
