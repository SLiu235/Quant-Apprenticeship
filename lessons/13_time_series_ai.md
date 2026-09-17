# Lesson 13 — Evaluate time-series models under regime change

Prerequisites: Lessons 8–9 and neural networks. Suggested effort: 6–8 hours, including the lab. Project: 5.

## More expressive models need a stronger experiment

Financial returns can have changing conditional mean, volatility and dependence. Weak stationarity means constant mean and lag-dependent covariance; it does not imply independent observations or stable market mechanisms. Prices often trend in level, while returns are closer to a useful modeling object. Differencing is a transformation with an economic interpretation, not a universal cure for nonstationarity.

For a supervised sequence model, define X_t=(x_{t−L},…,x_{t−1}) and target y_t at the actual decision horizon. Mask future observations, fit transformations on training data and make padding/missingness explicit. Normalizing each series using its full lifetime leaks future scale. A foundation time-series model adds pretraining provenance and historical-availability questions analogous to the LLM issue in Lesson 11.

A simple MLP can test nonlinear interactions before a transformer. For H=tanh(XW_1+b_1), prediction HW_2+b_2, minimizing mean squared error gives residual gradient 2(ŷ−y)/n; backpropagate through 1−H². Compare against ridge on identical data and selection budgets. If a bigger model wins only after dozens of undocumented trials, architecture is not the only explanation.

Increasing context length raises examples' overlap and memory use. Attention scores alone require O(B·heads·L²) storage in a conventional materialized implementation, though optimized kernels can change memory behavior. For B=8, heads=8, L=1,024 and float 32, one score tensor is 256 MiB. Activations, gradients, optimizer state and data add to that; model parameter count alone is not a memory budget.

## Worked experimental choice

Suppose ridge validation MSE is 1.00 and a small MLP's five seeds range.98–1.04 in the same normalized units. The evidence does not justify selecting only the.98 seed and reporting a 2% improvement. Prespecify whether the deployed procedure is an ensemble, a fixed seed or a seed-selection rule; evaluate that procedure. If market-date uncertainty dwarfs seed variance, more seeds cannot solve the data problem.

## Lab procedure

1. Build a causal length 20 sequence from the Project 3 panel; retain issuer/date identity.
2. Fit a tiny MLP on training data with a fixed seed and validation-only early stopping. Save the chosen checkpoint, not the final training iteration by habit.
3. Verify your gradient by finite differences on a tiny fixture before running the panel.
4. Compare with ridge/zero using the same chronological protocol. Record parameter count, runtime and all tried settings.
5. Read R1's deep-learning discussion and R2's leakage examples. For any foundation model extension, audit its model card and pretraining provenance first.

## Assignments

**A1.** Derive the two-layer gradient and compute the attention tensor memory above. Explain why a causal mask does not prevent leakage through a full-sample scaler.

**A2.** Train a small MLP with at most two hidden widths and one fixed training budget; compare all runs on development data. Include finite-difference and future-perturbation checks. Use the [numerical solutions](../reference/solutions.py) after your independent attempt.

**A3.** Write a model-selection decision for the five-seed example and a data/compute upgrade plan. Explain what a GPU can and cannot resolve.

Mastery check: you can reject a larger model based on comparable evidence without interpreting that as failure to use modern AI.

Check your work with the [answer key](../answers/13_time_series_ai.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
