# Lesson 8 — Make a simple model earn its complexity

Prerequisites: Lesson 7 and linear regression. Suggested effort: 5–7 hours, including the lab. Project: 3.

## A baseline is a scientific control

Start with unconditional frequency for classes or zero/rolling mean for returns. Then add a small interpretable price model. A richer model must improve the same target, eligible sample and decision horizon. Comparing an advanced model on liquid stocks against a baseline on every stock confounds model and sample.

The reference forms three features for each stock before day t: previous completed intraday return, previous five-day mean intraday return and previous 20-day standard deviation. Fit scaling on training observations only. Ridge minimizes mean squared error plus λ||w_nonintercept||². With standardized design Z, the normal equations are (ZᵀZ/n+λD)w=Zᵀy/n, where D leaves the intercept unpenalized. Scaling affects the penalty's economic meaning; leaking test variance still leaks information even without labels.

Return prediction often has tiny signal relative to noise. MSE and cross-sectional rank correlation answer different questions. A model can select relative winners while retaining market exposure, and a profitable long-only portfolio may simply benefit from a rising market. Report exposures, a benchmark and costs alongside predictive scores.

## Worked example

A strategy earns gross 8 bps/day and trades 0.8 of capital one-way daily. At 5 bps per unit turnover, estimated cost is 4 bps and net is 4 bps. A daily portfolio opened and fully closed with gross exposure 1 has turnover 2 under this convention, so cost is 10 bps. “Turnover” without a convention is not a usable number.

For exposure neutralization, regress a raw cross-sectional signal s on a full-rank exposure matrix B including an intercept: residual s−B(BᵀB)⁻¹Bᵀs is orthogonal to those columns in-sample. This is a signal transformation, not proof the final constrained portfolio is neutral or that future betas are known.

## Lab procedure

1. Run Project 3 and inspect its chronological refit log, validation scores and cost table.
2. Implement ridge independently on a small synthetic matrix; compare against the normal equations.
3. Reproduce a single actual prediction from its training scaler, weights and feature values.
4. Add zero-return and training-mean baselines on identical observations. Keep your additions labeled development analysis.
5. Read R1's regularization chapter and R3's model-comparison setup.

## Assignments

**A1.** Derive the ridge normal equations and both cost examples. Explain why λ changes meaning if features are rescaled without retraining.

**A2.** Produce a prediction ledger with decision date, last training-label date, model/scaler ID, prediction, target, hypothetical position and cost. Test that perturbing a future return cannot change an earlier prediction.

**A3.** Interpret Project 3's result against zero prediction. Explain why negating a losing signal after seeing its evaluation is a new hypothesis, not recovered out-of-sample alpha. Specify an exposure diagnostic.

Mastery check: the baseline has the same data rights as the candidate and its negative result remains in the experiment ledger.

Check your work with the [answer key](../answers/08_baseline.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
