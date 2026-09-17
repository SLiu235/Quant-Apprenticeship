# Project 3 — Build and challenge a price-only forecasting procedure

Lessons: 07–09. Integration effort after lessons: 12–18 hours. Workspace connection: QuantPipeline.

## Research question and input

Does a simple causal price model improve same-day intraday-return prediction over zero/training-mean baselines? Use the existing real Yahoo bars for ASML, MU, SNDK and WDC. These are four retrospectively selected Nasdaq-listed issuers, not a point-in-time Nasdaq universe. Same-day close/open returns do not capture overnight trading.

## Build it step by step

1. Write a coverage/source report before taking the common-date intersection. Preserve raw hashes.
2. Build prior 1-day return, prior 5-day mean and prior 20-day volatility features using only completed sessions.
3. Split ordered dates 60/20/20; fit scalers on training only and select ridge penalty from(.01,.1,1) on validation.
4. Evaluate a fixed every 20-date refit schedule using all labels available before each refit. Record dates, scalers and fitted weights.
5. Compare model/zero/training-mean MSE on identical observations. Add hypothetical positions only as a separate economic exercise.
6. Report gross/net returns under 0/5/10/25 bps one-way costs and explicit turnover. Register every variant in the ledger.

## Student deliverables

Coverage and source manifest, reproducible model code, prediction ledger, split/refit log, tests, full candidate table and memo. Include a future-perturbation test. Any change made after seeing this reference is development work.

## Worked project and interpretation

The snapshot has 394 common dates; 20 warm-up dates leave 374 modeled dates. The final 75 dates run May 22–September 9, 2026. Validation selectsλ=.01. Model MSE≈.001743422 exceeds zero's .001707953. A naive sign position with unit gross exposure earns about −3.93535 bps/day before costs and −13.93535 bps at 5 bps one-way cost. Its break-even cost is negative.

The sample decision is to reject promotion of this particular rule. It is not evidence that price forecasting is universally impossible. The sign-to-position mapping is intentionally naive, open/close prices are assumed marks, and borrow/impact/financing are not modeled. Reversing the sign because this result is negative creates a new hypothesis requiring fresh evidence.

## Acceptance and answer guidance

All transforms and fits must obey the availability clock. Model comparison must preserve issuer/date populations. The refit log should show last_label_date strictly earlier than decision_date. Costs must count opening and closing trades for this daily-flat strategy. Keys 07–09 explain the split, ridge derivation, search budget and interpretation.

Extension: add the tiny MLP from Lesson 13 on development data with a fixed candidate budget. Report every width/seed and comparable baselines; a larger model earns no automatic credit. For a broad market conclusion, first acquire a historical universe, corporate-action and delisting dataset rather than scaling this four-stock panel.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 3
```

[Complete reference code](../reference/p03_baseline.py) · [Recorded result](../outputs/p03_baseline.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
