# Optional assessment 06 — Transaction costs and execution simulation

Use this when you choose to self-assess or request a mentor review. It is not a prerequisite quiz. Keep your attempt before opening the [hints and key](../../answers/integrated/06_execution_microstructure.md).

## Part A — Numerical or conceptual case

A buy for 80 shares has 30 filled and 50 live. A cancel is requested; 10 more fill before acknowledgment. How many shares should the acknowledgment cancel? Should a repeated fill ID change inventory?

Your calculation and assumptions:

```text
Answer:
Assumptions:
What this does not establish:
```

## Part B — Debugging evidence

Reproduce a partial fill followed by cancel request, another fill and cancel acknowledgment. After every event require original quantity = filled + cancelled + live remainder, using consistent side conventions. Inject a duplicate fill and a sequence gap.

Submit a minimal reproducer, expected behavior, at least two hypotheses, the evidence that distinguishes them, and a regression test. An honest unresolved result with a disciplined investigation is useful review evidence.

## Part C — Investment or architecture decision

A short-lived signal competes with a wide spread and thin depth. Choose immediate execution, passive posting, a staged schedule or no trade. State the assumptions about signal decay, queue position and adverse selection that drive your choice.

Write at most 300 words. Include an alternative and a condition that would reverse your choice.

## Part D — Project evidence review

Check the deliverables in [Project 06](../../projects/integrated/06_execution_microstructure.md). For each completion criterion, link evidence or mark it unverified. Use the [optional common rubric](../SELF_PACED.md); passing reference tests alone is not evidence of independent competence.
