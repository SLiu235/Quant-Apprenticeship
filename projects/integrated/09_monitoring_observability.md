# Integrated project 09 — Monitoring, drift and incident response

[Module notes](../../modules/09_monitoring_observability.md) · [Optional self-assessment](../../assessments/integrated/09_monitoring_observability.md)

## Problem and requirements

Detect actionable failures, preserve diagnostic evidence and restore operation through explicit checks.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add a stateful monitor for duplicate events, source sequence gaps, model/schema mismatch and delayed labels. Create an offline dashboard/report and an alert-state reducer with acknowledgment and resolution. Measure false alerts on fixed fixtures rather than choosing thresholds after inspecting the worst incident.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_09/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

monitor_rules.py; alert catalog; incident.json; report; runbook; fault-injection tests; bug journal entry

## Acceptance evidence

Actionable alert catalog; freshness/NaN/reconciliation tests; incident timeline; restart/resume criteria; concise postmortem; clear separation between operational failure and investment underperformance.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Begin at the earliest failed invariant, not the last exception. Preserve the offending event, source version and clock. Form competing explanations and identify the smallest observation that distinguishes them.

## Worked code and limitations

Reference source: `apprentice_system/monitoring.py`. Run `python3 -m apprentice_system.run --stage 9` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/06_research_ownership.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
