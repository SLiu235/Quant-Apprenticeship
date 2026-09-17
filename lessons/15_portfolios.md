# Lesson 15 — Optimize a constrained portfolio and test its economics

Prerequisites: Lessons 4, 8 and 14. Suggested effort: 6–8 hours, including the lab. Project: 5.

## An optimizer magnifies estimation errors

A mean-variance decision solves maximize μᵀw−γwᵀΣw/2−cost (w−w_old), subject to budget, leverage, concentration and other limits. Forecast μ, covariance Σ, penalty γ and costs must use compatible horizons and return units. Optimizing basis-point means against decimal variance without conversion can produce wildly wrong positions while the solver reports success.

Sample covariance is noisy, especially when assets are numerous relative to dates. Shrinkage combines it with a structured target: Σ_hat=(1−λ)S+λT. The reference uses a fixed diagonal target and λ=.5 plus a tiny diagonal stabilizer. This is a teaching rule; it is not the estimated optimal Ledoit–Wolf procedure in R13. Check eigenvalues, conditioning and sensitivity to λ and estimation windows.

Without bounds, minimum-variance fully invested weights are Σ⁻¹1/(1ᵀΣ⁻¹1), provided the inverse exists. Constraints alter the solution; clipping unconstrained weights and renormalizing generally does not solve the constrained problem. Use a suitable solver and verify primal feasibility, objective and, when relevant, optimality conditions. A successful status is one piece of evidence, not a complete validation.

## Worked example

Two uncorrelated assets have variances 1 and 4 in the same units. Unconstrained minimum-variance weights are .8 and .2; portfolio variance=.8. With a maximum weight.6, optimum is (.6,.4), variance=.36+.64=1.0. Equal weight variance is 1.25. A valid optimizer sacrifices some unconstrained variance reduction to satisfy the concentration constraint.

The reference holds long-only weights summing to 1 with a.5 cap across four names, opens and closes every day, and subtracts an illustrative 10 bps round-trip at 5 bps one-way. It forecasts risk rather than expected alpha. Its positive gross return can be market exposure in a selected universe. Capacity additionally depends on participation, depth and impact; daily volume is not guaranteed liquidity at your decision time.

## Lab procedure

1. Derive and solve the two-asset example by hand.
2. Run Project 5 and verify bounds, sum and covariance condition at every decision.
3. Compare minimum variance and equal weight on identical dates, reporting risk, return, costs and exposure.
4. Stress risk estimates, one-way costs and position caps using development data. Record all variants.
5. Read R13 and R14's quadratic-program/optimality material.

## Assignments

**A1.** Derive the unconstrained solution with a Lagrange multiplier and reproduce the bounded example.

**A2.** Add solver checks against the analytical two-asset case and the equal-weight feasible objective. Implement turnover/cost reporting under a clearly defined intraday or carried-position convention.

**A3.** A proposal allocates$5m to a security with $2m observed volume in the intended interval and a 5% participation cap. Calculate the maximum allowed notional and explain the proposal's feasibility. State what the reference's positive mean does not establish.

Mastery check: your decision obeys constraints in economic units and remains defensible when forecast inputs are perturbed.

Check your work with the [answer key](../answers/15_portfolios.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
