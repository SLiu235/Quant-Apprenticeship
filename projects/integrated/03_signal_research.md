# Integrated project 03 — Signal research and validation

[Module notes](../../modules/03_signal_research.md) · [Optional self-assessment](../../assessments/integrated/03_signal_research.md)

## Problem and requirements

Evaluate a hypothesis against simple baselines without allowing future labels or model selection to contaminate the result.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add a rolling-window model and a purged split generator operating on explicit label intervals. Implement a date-block comparison using reference/p01_audit.py as a separate example. Log variants before evaluation and create a report that distinguishes software correctness from empirical support.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_03/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

hypothesis.md; split_diagram.md; split_generator.py; variant_ledger.md; metrics.json; leakage tests; research memo

## Acceptance evidence

Frozen hypothesis and variant ledger; matched baseline comparison; chronological split diagram; leakage mutation test; uncertainty interpretation; a negative-result decision as defensible as a positive one.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Multiply future prices by three and verify that all preceding forecasts are unchanged. If not, find the earliest changed feature, fitted parameter or label inclusion. Introduce a five-session target and inspect label maturity explicitly.

## Worked code and limitations

Reference source: `apprentice_system/research.py`. Run `python3 -m apprentice_system.run --stage 3` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/02_research_discovery.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
