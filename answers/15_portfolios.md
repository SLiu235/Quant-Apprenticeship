# Lesson 15 answer key — Optimize a constrained portfolio and test its economics

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

MinimizewᵀΣw with 1ᵀw=1. Stationarity 2Σw−η1=0 givesw∝Σ⁻¹1; normalization yields the formula. For diagonal(1,4), inverse weights 1 and .25 normalize to (.8,.2), variance .64+.16=.8. Withw 1≤.6, convexity places the optimum at (.6,.4), variance 1.0. This is lower than equal-weight 1.25 while respecting the constraint.

## A2

The reference optimizer is scaled for numerical conditioning and enforces sum 1, nonnegative weights and .5 caps. It must return an objective no worse than the equal-weight feasible candidate within tolerance. For the two-asset exercise use cap.6, not the four-asset reference's.5. Verify with a separate grid or analytical result. Intraday flat-to-flat turnover is 2Σ|w|; a carried portfolio uses actual changes from drifted pretrade weights, with initial/final liquidation handled separately. Reporting Σ|w_t−w_{t−1}| for a daily-flat strategy understates cost.

## A3

5%×$2m=$100,000 in that observed interval; a$5m order is 50 times the cap. Even$100,000 is only an upper bound under the stipulated volume/cap, not proof of execution quality. The sample's mean return does not establish market-neutral alpha, broad-universe performance, scalable fills or robust tail risk. Reference minimum-variance realized daily standard deviation≈221.16 bps versus equal≈298.57 bps in the selected sample; assess this as a descriptive teaching comparison, not a deployment approval.

Repair: test a unit conversion error deliberately. If positions change because the same economics were restated in bps, the objective is inconsistent.
