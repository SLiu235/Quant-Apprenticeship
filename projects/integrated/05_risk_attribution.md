# Integrated project 05 — Risk, scenarios and P&L attribution

[Module notes](../../modules/05_risk_attribution.md) · [Optional self-assessment](../../assessments/integrated/05_risk_attribution.md)

## Problem and requirements

Explain portfolio losses in dollars, distinguish exposures from scenarios, and reconcile P&L independently.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add dividend and financing events to an independent ledger and extend attribution accordingly. Add rolling factor exposure estimation using the existing numerical environment, then distinguish accounting attribution from estimated factor attribution in the report.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_05/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

risk_policy.md; cashflow events; attribution.py; reconciliation.json; factor/scenario report; hand calculation; regression tests; postmortem

## Acceptance evidence

Reconciled daily P&L; explicit costs/cashflows; exposure and scenario reports; named residual limitations; one failure postmortem; no unexplained accounting residual.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Create a one-dollar discrepancy and test cash entries, quantities, mark timestamps and price units. Find the first event where ledger equity and independently explained P&L diverge. Do not plug the residual into an unexplained bucket.

## Worked code and limitations

Reference source: `apprentice_system/risk.py`, `apprentice_system/execution.py`. Run `python3 -m apprentice_system.run --stage 5` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/04_economic_value.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
