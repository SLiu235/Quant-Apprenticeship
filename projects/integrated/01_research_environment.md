# Integrated project 01 — A trustworthy research run

[Module notes](../../modules/01_research_environment.md) · [Optional self-assessment](../../assessments/integrated/01_research_environment.md)

## Problem and requirements

Produce a reproducible research result and explain exactly which decision it can support.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add a configuration file whose validated contents enter the run identity. Make the output directory irrelevant to identity. Detect a changed input byte and reject nonfinite parameters before computation.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_01/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

contract.md; architecture.md; config.json; run command; two matching manifests; one hand-check.md; tests for invalid configuration; memo.md

## Acceptance evidence

A research contract, requirements sketch, reproducible command, manifest, independent numerical check and a short claim/limitation memo. Positive P&L is not required.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Run identical input bytes from two fresh output directories. If results differ, isolate data, parameters, numerical runtime and hidden state in that order. Change one parameter and confirm the identity changes. Preserve the original discrepancy before repairing it.

## Worked code and limitations

Reference source: `apprentice_system/core.py`, `apprentice_system/run.py`. Run `python3 -m apprentice_system.run --stage 1` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/01_edge_and_data.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
