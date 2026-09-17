# Integrated project 04 — Portfolio construction under uncertain inputs

[Module notes](../../modules/04_portfolio_construction.md) · [Optional self-assessment](../../assessments/integrated/04_portfolio_construction.md)

## Problem and requirements

Translate forecasts into constrained positions and explain how uncertainty, turnover and costs alter the allocation.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Implement equal-weight and no-trade-band policies with identical execution assumptions. Add a small turnover penalty to the existing optimizer, check feasibility independently, and compare forecast/covariance perturbations. Treat Black-Litterman or robust optimization as an extension only after defining credible views and uncertainty.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_04/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

mandate.md; portfolio_policy.py; forecast sensitivity table; turnover/cost comparison; constraint tests; decision record

## Acceptance evidence

Explicit objective/constraints; current-to-target order accounting; sensitivity report; cost/turnover comparison; handling of no signal and infeasible requests; no claims of beta neutrality without measured exposures.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Make every alpha zero, make one alpha very large, and perturb forecasts slightly. Test whether allocation stays finite, feasible and proportionate. Construct a cap-and-renormalize counterexample and identify which postcondition fails.

## Worked code and limitations

Reference source: `apprentice_system/portfolio.py`, `apprentice_system/risk.py`. Run `python3 -m apprentice_system.run --stage 4` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/04_economic_value.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
