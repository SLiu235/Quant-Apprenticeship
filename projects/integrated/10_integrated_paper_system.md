# Integrated project 10 — Integrated paper portfolio and investment committee

[Module notes](../../modules/10_integrated_paper_system.md) · [Optional self-assessment](../../assessments/integrated/10_integrated_paper_system.md)

## Problem and requirements

Own a complete simulation run, defend its investment interpretation and explain what evidence is still missing.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Integrate your independently built components through the same contracts. Add a cash baseline and a feasible equal-weight baseline with identical simulator settings, match forecast and inventory horizons, compare low/high cost regimes, and write the investment committee decision. Keep real-data experiments in a separate run namespace.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_10/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

integrated run manifest; event replay; accounting reconciliation; baseline/cost/stress reports; incident replay; committee_memo.md; five updated learning journals

## Acceptance evidence

One-command replay; reconciled event history; matched baselines; horizon-consistent accounting or an explicit attribution split; stress/cost sensitivity; incident recovery evidence; committee memo and an honest skills-gap update. No automatic promotion or capital deployment.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Inject a mismatch between forecast version and portfolio run, a duplicate fill and a stale mark. Trace the earliest violated contract. Reconstruct expected balances from the immutable evidence and explain whether recovery changes the investment conclusion.

## Worked code and limitations

Reference source: `apprentice_system/run.py`. Run `python3 -m apprentice_system.run --stage 10` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/06_research_ownership.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
