# Optional assessment 03 — Signal research and validation

Use this when you choose to self-assess or request a mentor review. It is not a prerequisite quiz. Keep your attempt before opening the [hints and key](../../answers/integrated/03_signal_research.md).

## Part A — Numerical or conceptual case

You fit a scaler on all dates, then train the model on the first 70% and evaluate on the final 30%. Is the result clean? Separately, a training label ends after the next forecast decision: is it eligible?

Your calculation and assumptions:

```text
Answer:
Assumptions:
What this does not establish:
```

## Part B — Debugging evidence

Multiply future prices by three and verify that all preceding forecasts are unchanged. If not, find the earliest changed feature, fitted parameter or label inclusion. Introduce a five-session target and inspect label maturity explicitly.

Submit a minimal reproducer, expected behavior, at least two hypotheses, the evidence that distinguishes them, and a regression test. An honest unresolved result with a disciplined investigation is useful review evidence.

## Part C — Investment or architecture decision

Choose a zero/linear baseline or a transformer for a small selected panel. Specify the evidence, data scale and evaluation improvement that would earn the complex model a place.

Write at most 300 words. Include an alternative and a condition that would reverse your choice.

## Part D — Project evidence review

Check the deliverables in [Project 03](../../projects/integrated/03_signal_research.md). For each completion criterion, link evidence or mark it unverified. Use the [optional common rubric](../SELF_PACED.md); passing reference tests alone is not evidence of independent competence.
