# Optional assessment 02 — Point-in-time data and feature pipeline

Use this when you choose to self-assess or request a mentor review. It is not a prerequisite quiz. Keep your attempt before opening the [hints and key](../../answers/integrated/02_point_in_time_data.md).

## Part A — Numerical or conceptual case

An event occurs at 12:00 UTC, is published at 12:01, and reaches your feed at 12:03. Your decision is 12:02. Can the feature use it? A correction arrives at 15:00; which revision belongs in a 14:00 replay?

Your calculation and assumptions:

```text
Answer:
Assumptions:
What this does not establish:
```

## Part B — Debugging evidence

Inject a revision received after the decision and inspect the earliest changed feature. Assert that earlier decisions remain byte-identical. Inject a duplicate key and a timezone-naive timestamp; determine where they should be rejected.

Submit a minimal reproducer, expected behavior, at least two hypotheses, the evidence that distinguishes them, and a regression test. An honest unresolved result with a disciplined investigation is useful review evidence.

## Part C — Investment or architecture decision

Choose JSON, Parquet with DuckDB, or PostgreSQL for immutable daily snapshots used by one researcher. Decide first. Include concurrent writers, transactional requirements, expected scan size and recovery in the comparison.

Write at most 300 words. Include an alternative and a condition that would reverse your choice.

## Part D — Project evidence review

Check the deliverables in [Project 02](../../projects/integrated/02_point_in_time_data.md). For each completion criterion, link evidence or mark it unverified. Use the [optional common rubric](../SELF_PACED.md); passing reference tests alone is not evidence of independent competence.
