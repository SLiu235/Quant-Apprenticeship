# Integrated project 06 — Transaction costs and execution simulation

[Module notes](../../modules/06_execution_microstructure.md) · [Optional self-assessment](../../assessments/integrated/06_execution_microstructure.md)

## Problem and requirements

Evaluate the complete execution mandate, including partial fills, adverse selection and the cost of not trading.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Implement a persistent order state machine and two schedulers: TWAP and forecast-volume VWAP. Keep forecast volume separate from realized replay volume. Add a cancel-in-flight event fixture, adverse-selection markouts and a spread/impact sensitivity grid. Use reference/p02_replay.py for the stipulated passive queue baseline.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_06/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

order_reducer.py; schedule.py; synthetic event tape; tca.json; cost-model assumptions; conservation/retry tests; execution decision memo

## Acceptance evidence

Order conservation; buy/sell cost checks; explicit fill assumptions; delay/spread/impact/fees/opportunity decomposition; cost sensitivity; queue and cancel-race tests; a no-trade case.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Reproduce a partial fill followed by cancel request, another fill and cancel acknowledgment. After every event require original quantity = filled + cancelled + live remainder, using consistent side conventions. Inject a duplicate fill and a sequence gap.

## Worked code and limitations

Reference source: `apprentice_system/execution.py`. Run `python3 -m apprentice_system.run --stage 6` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/04_economic_value.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
