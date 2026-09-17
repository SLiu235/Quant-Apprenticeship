# Optional assessment 07 — Production data and model pipelines

Use this when you choose to self-assess or request a mentor review. It is not a prerequisite quiz. Keep your attempt before opening the [hints and key](../../answers/integrated/07_production_pipelines.md).

## Part A — Numerical or conceptual case

The database commit succeeds but the client times out. What should the retry send, and what evidence distinguishes harmless retry from conflicting state?

Your calculation and assumptions:

```text
Answer:
Assumptions:
What this does not establish:
```

## Part B — Debugging evidence

Terminate a subprocess after committing an event but before acknowledging it, then retry. Compare cash, inventory and event count. Corrupt an artifact and verify that reuse fails visibly. Separate expected duplicates from conflicting duplicates.

Submit a minimal reproducer, expected behavior, at least two hypotheses, the evidence that distinguishes them, and a regression test. An honest unresolved result with a disciplined investigation is useful review evidence.

## Part C — Investment or architecture decision

Choose one scheduled process with SQLite/files, a queue plus workers, or distributed services. Give an observed concurrency, latency or reliability requirement for each added component.

Write at most 300 words. Include an alternative and a condition that would reverse your choice.

## Part D — Project evidence review

Check the deliverables in [Project 07](../../projects/integrated/07_production_pipelines.md). For each completion criterion, link evidence or mark it unverified. Use the [optional common rubric](../SELF_PACED.md); passing reference tests alone is not evidence of independent competence.
