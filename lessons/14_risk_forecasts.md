# Lesson 14 — Forecast uncertainty and test calibration

Prerequisites: Lessons 3 and 13. Suggested effort: 5–7 hours, including the lab. Project: 5.

## A good mean forecast can still size risk badly

A conditional variance forecast v_t predicts E[(r_t−μ_t)² | I_t]. In a mean-zero approximation, realized r_t² is a noisy proxy. A single quiet return is not a precise estimate of tomorrow's variance; yesterday's squared return can be nearly zero and produce dangerously small forecasts. Compare robust rolling or exponentially weighted estimates before complex volatility networks.

QLIKE in this course is log(v_t)+r_t²/v_t, with v_t>0 and returns in decimals. Taking conditional expectation and differentiating gives 1/v−E[r²]/v², minimized at v=E[r²]. This is a proper target for the conditional second moment under this formulation. It is not a return-mean score. Negative QLIKE values are possible because log(v) is negative for small decimal variances; absolute values depend on units.

Calibration asks whether predicted distributions agree with realized frequencies or moments. For probability forecasts, inspect reliability bins and proper scores; bins need counts and uncertainty. For variance, compare realized/predicted second moments and conditional slices. An aggregate ratio near 1 can hide underprediction on volatile days and overprediction on quiet days. VaR exceedance rates need both unconditional frequency and clustering checks; a correct rate alone does not prove tail loss adequacy.

## Worked example

Suppose r²=.0004. Forecast v=.0004 gives log(.0004)+1≈−6.824046. Forecast v=.0001 gives log(.0001)+4≈−5.210340, worse for this observation. One observation does not establish which model predicts better in expectation. A floor keeps division finite but is part of the model and must not be tuned on the final sample.

Project 5 compares a 20-day rolling second moment against yesterday's square, using a fixed tiny floor. The latter's huge loss is a lesson about an unstable baseline, not proof of sophisticated risk modeling. The reference also includes a fixed-decay EWMA comparator; reproduce it independently before a stronger empirical claim.

## Lab procedure

1. Run Project 5 and reconcile its risk target with Project 3's intraday return horizon.
2. Compute a rolling and EWMA second moment using only completed prior returns. Define EWMA initialization and decay in advance.
3. Produce calibration tables for low/high predicted risk, with observations and dates per cell.
4. Report QLIKE, empirical risk, tail exceedances under an explicitly assumed distribution and the sensitivity to variance floors.
5. Read R13's motivation for noisy risk estimation; distinguish univariate forecasting from cross-asset covariance estimation.

## Assignments

**A1.** Derive the expected-QLIKE minimizer and calculate the two worked losses. Explain units and mean-zero assumptions.

**A2.** Add EWMA with prespecified decay. Submit paired date losses, a calibration table and a floor sensitivity analysis labeled development. Compare against rolling 20, not just the fragile previous-square model.

**A3.** Explain why the reference's aggregate second-moment ratio≈1.008 does not prove tail calibration or portfolio safety. Give a two-regime counterexample.

Mastery check: risk forecasts are evaluated at the same horizon and exposure definition as the proposed decision.

Check your work with the [answer key](../answers/14_risk_forecasts.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
