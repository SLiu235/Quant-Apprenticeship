# Project 1 — Independently audit a recent public-signal study

Lessons: 01–03. Integration effort after lessons: 8–12 hours. Workspace connection: BehaviorIRL.

## Research question and input

Does the frozen public-text feature improve a preopen response forecast over the frozen market-feature baseline on eligible issuer-days? Use the saved real prediction file, protocol and prepared-data audit. Do not refit or refresh the raw data while reproducing this result. This study uses 2025–February 2026 social/price pairs; its saved evaluation is already inspected.

## Build it step by step

1. Finish Lessons 01–03 and record your contract before inspecting the answer-key numbers.
2. Implement independent CSV parsing, probability checks and episode/model joins. Assert the class-column mapping with a hand fixture.
3. Produce NLL, Brier and accuracy for frequency, market, public and graph.
4. Form public-minus-market paired losses, compare row/date weighting and implement the specified block bootstrap.
5. Audit one actual observation's information clock. Separate observed publication from assumed availability and note comment-collection bias.
6. Write a recommendation and one next experiment; do not turn an unfavorable result into an immediate hyperparameter search.

## Student deliverables

`audit.py`, `metrics.json`, `availability_example.md`, `manifest.json` and an 800-word maximum `memo.md`. Store them in `submissions/project_01/`. Include a single run command and failure tests. Your memo must distinguish response prediction, participant actions, reward identification and trading economics.

## Worked project and interpretation

The runnable reference independently recomputes the saved file. It finds NLL .94566558 for frequency, .96057626 for market, .97737307 for public and .98673748 for graph. Public-minus-market is +.01679681 per row and +.01464994 per equally weighted date. The primary three-date interval is[.00642250,.02457990]. Negative would favor public, so this result is unfavorable.

A sample conclusion: “The fixed text feature did not improve probabilistic prediction in this selected recent sample. Frequency was stronger than both market and text, making the market baseline itself worth questioning. The graph analysis remains a biased discussion diagnostic. We should not promote the model or infer actor motives. A prospective panel with actual receipts and fixed sampling is a candidate next experiment if its expected information value justifies acquisition.”

## Acceptance and answer guidance

Full credit requires independently generated metrics, matched populations, correctly signed/date-weighted comparison and the same declared bootstrap algorithm. Numeric tolerances:1e−9 for scores/means; discuss RNG differences explicitly for intervals. A correct number with an “IRL validated” conclusion fails the interpretation gate. Keys 01–03 give the arithmetic, selection explanation and debugging sequence.

Common repairs: swapped labels → fixture; different mean → weighting; narrower interval → resampling unit; misplaced confidence → collection/clock audit. Extension: compare alternate dependence blocks as labeled sensitivity, not a new primary selected after seeing results.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 1
```

[Complete reference code](../reference/p01_audit.py) · [Recorded result](../outputs/p01_audit.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
