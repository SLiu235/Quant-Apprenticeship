# Project 5 — Forecast risk and allocate under constraints

Lessons: 13–15. Integration effort after lessons: 12–20 hours. Workspace connection: QuantTimeLearn and QuantCUDA.

## Research question and input

Can a simple risk model improve uncertainty estimates and support a transparent constrained allocation? Use the real intraday return panel, with a synthetic analytical optimization fixture as an independent oracle. Risk forecasting, portfolio risk reduction and expected alpha are separate claims.

## Build it step by step

1. Run the tiny MLP/gradient exercise from Lesson 13 to practice controlled nonlinear modeling, then keep the risk project anchored to simple comparators.
2. Forecast second moments using rolling 20, yesterday's square and a declared EWMA. Use only prior completed returns and a fixed variance-floor policy.
3. Compare QLIKE on identical dates and make conditional calibration tables with counts.
4. Estimate rolling 60-day covariance; apply fixed diagonal shrinkage and inspect numerical condition.
5. Solve long-only minimum variance with sum 1 and maximum weight.5. Check against equal-weight feasible objective and the analytical two-asset exercise.
6. Report gross returns, volatility, costs, turnover and concentration; label daily-flat open/close execution assumptions.

## Student deliverables

Risk forecasts and paired losses, calibration table, covariance/weight ledger, solver tests, cost table and memo. Include all floor/decay/shrinkage choices in the experiment ledger. Preserve primary settings while labeling sensitivities development-only.

## Worked project and interpretation

The reference evaluates 334 dates from May 12, 2025 to September 9, 2026. Rolling 20 QLIKE is about −5.90865; yesterday's squared-return baseline is extremely poor because small denominators cause large penalties. The reference EWMA(.94) QLIKE is about −5.89578. Comparing these two stable forecasts is more informative than celebrating the fragile baseline's failure; the small difference still needs paired uncertainty. Aggregate realized/predicted second moment is about 1.0081, which does not establish conditional or tail calibration.

The constrained minimum-variance portfolio has sample daily standard deviation≈221.16 bps versus equal weight≈298.57 bps. Its positive gross mean is descriptive and can reflect selected long market exposure. At 5 bps one-way costs, the reference subtracts 10 bps/day; no actual auction-fill, impact or borrowing study has been conducted.

## Acceptance and answer guidance

Forecasts must use the correct horizon/units. Keep second moments distinct from centered covariance. Bounds and budget must hold at every decision; compare solver output with an independent analytical fixture. A stronger risk baseline is required in the student project so yesterday's fragile square cannot be the sole competitor. Keys 13–15 provide derivations and expected numerical checks.

Extension: add probabilistic/deep volatility forecasts only after an adequately controlled rolling/EWMA comparison. An optional single GPU changes runtime, not the need for independent market-date evidence. Larger-universe allocation requires a point-in-time universe and realistic capacity data.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 5
```

[Complete reference code](../reference/p05_risk.py) · [Recorded result](../outputs/p05_risk.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
