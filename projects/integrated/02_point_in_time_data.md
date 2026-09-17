# Integrated project 02 — Point-in-time data and feature pipeline

[Module notes](../../modules/02_point_in_time_data.md) · [Optional self-assessment](../../assessments/integrated/02_point_in_time_data.md)

## Problem and requirements

Reconstruct the information set available at a historical decision and preserve that view after later corrections.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Add a revision stream and a storage adapter using sqlite3 first or DuckDB if already installed. Store multiple versions without overwriting. Implement a configurable missing-symbol policy that fails or abstains explicitly, then compare SQL and Python results on the same fixture.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_02/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

schema.md; data_adapter.py; asof_query.sql; revision fixture; lineage.json; missing-data policy; tests; availability memo

## Acceptance evidence

An auditable as-of join; duplicate and schema checks; a future-revision invariance test; explicit missing-data and universe policies; lineage for one feature.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Inject a revision received after the decision and inspect the earliest changed feature. Assert that earlier decisions remain byte-identical. Inject a duplicate key and a timezone-naive timestamp; determine where they should be rejected.

## Worked code and limitations

Reference source: `apprentice_system/data.py`. Run `python3 -m apprentice_system.run --stage 2` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/01_edge_and_data.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
