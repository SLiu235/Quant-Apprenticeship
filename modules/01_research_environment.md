# Module 01 — A trustworthy research run

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/01_research_environment.md) · [Optional assessment](../assessments/integrated/01_research_environment.md)

## Objective

Produce a reproducible research result and explain exactly which decision it can support.

## Prerequisites and pace

CFA/CQF/AI concepts and basic Python; practical ability is initially unverified. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

A research contract fixes the question, population, information cutoff, forecast horizon, comparison, loss function, exclusions and decision before examining outcomes. Separate a software acceptance check from a claim about investment performance. A manifest binds data bytes, code bytes, parameters and runtime to a result; a seed alone does not do this. Pure calculation functions make assumptions inspectable, while the runner owns file access and orchestration.

## Mental models

Treat a backtest as an argument supported by a chain of evidence. Every transformation is a premise. Ask which premise, if false, would overturn the conclusion. Determinism makes mistakes reproducible; it does not make them correct.

## Worked example

An experiment predicts an up move with probability 0.60. Conditional gains are 1 bp and conditional losses are 5 bps. Expected gross return is 0.60×1 − 0.40×5 = −1.4 bps. After a stipulated 2 bp round-trip cost, the long trade has expected return −3.4 bps. Predicting the more likely direction correctly does not establish a good trade.

## Implementation

Create a single-command runner, a research contract and a manifest. Trace one output back to the input rows and parameters that produced it. Keep calculations independent of output paths and report economic units explicitly.

Read the contracts and trace one observation before editing. Reference code: [core.py](../apprentice_system/core.py) · [run.py](../apprentice_system/run.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 1 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Hidden notebook state; overwritten inputs; a seed recorded without data versions; broad claims from a selected population; changing the success criterion after seeing results.

## Debugging exercise

Run identical input bytes from two fresh output directories. If results differ, isolate data, parameters, numerical runtime and hidden state in that order. Change one parameter and confirm the identity changes. Preserve the original discrepancy before repairing it.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose between a notebook-only experiment, a Python package with a CLI, and several services for a three-asset daily prototype. Write the operational requirement that could justify each extra boundary before reading the reference.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

A research contract, requirements sketch, reproducible command, manifest, independent numerical check and a short claim/limitation memo. Positive P&L is not required.

## Deeper teaching and existing worked projects

[01 research contract](../lessons/01_research_contract.md) · [19 research software](../lessons/19_research_software.md) · [22 capstone protocol](../lessons/22_capstone_protocol.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/01_edge_and_data.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
