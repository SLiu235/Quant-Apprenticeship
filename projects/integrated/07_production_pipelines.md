# Integrated project 07 — Production data and model pipelines

[Module notes](../../modules/07_production_pipelines.md) · [Optional self-assessment](../../assessments/integrated/07_production_pipelines.md)

## Problem and requirements

Persist validated artifacts and recover state after retry or restart without silent duplication.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add job states, feature-schema hashes and an atomic active-model pointer. Write subprocess crash-injection tests around commit/publication boundaries. Provide a simple local CI command and optionally a container; justify any service or scheduler you add.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_07/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

pipeline.py; schema/model manifests; event database; restart comparison; crash tests; rollback runbook; architecture decision

## Acceptance evidence

Stable IDs; restart reconstruction; corruption detection; model/schema contract; documented failure boundaries and rollback; tests of an actual interrupted subprocess in your extension.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Terminate a subprocess after committing an event but before acknowledging it, then retry. Compare cash, inventory and event count. Corrupt an artifact and verify that reuse fails visibly. Separate expected duplicates from conflicting duplicates.

## Worked code and limitations

Reference source: `apprentice_system/pipeline.py`, `apprentice_system/run.py`. Run `python3 -m apprentice_system.run --stage 7` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/03_predictive_ai.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
