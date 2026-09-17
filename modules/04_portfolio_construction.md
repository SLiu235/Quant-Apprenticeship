# Module 04 — Portfolio construction under uncertain inputs

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/04_portfolio_construction.md) · [Optional assessment](../assessments/integrated/04_portfolio_construction.md)

## Objective

Translate forecasts into constrained positions and explain how uncertainty, turnover and costs alter the allocation.

## Prerequisites and pace

Module 3: validated forecasts; basic execution costs and risk units. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Keep forecast generation separate from portfolio policy. A useful objective is wᵀα − λwᵀΣw − TC(w−w₀) − γTailRisk(w), subject to mandate constraints. Specify units and horizon for every term; λ and γ encode preferences, not facts inferred from an attractive result. A weight is not an order. Convert target dollars to shares using a price available at the sizing decision and then subtract existing holdings. Cash is a legitimate residual when the case for risk is weak.

## Mental models

An optimizer magnifies whatever the inputs insist is precise. Start with a transparent allocation rule, perturb the forecasts and covariance, and ask whether the proposed trade survives reasonable uncertainty. Never renormalize after capping without checking that the cap still holds.

## Worked example

With $100,000 equity, a 20% target and a $50 sizing price, target inventory is 400 shares. If 350 are already held, the order is +50. The execution price may differ, so realized weights and cash must be checked after fills. A drifted current portfolio is not identical to yesterday’s target weights.

## Implementation

Inspect the long-only capped-conviction baseline with residual cash. Compare it with equal weighting and the existing shrinkage/minimum-variance example. Add a turnover-aware policy before adding more elaborate optimization.

Read the contracts and trace one observation before editing. Reference code: [portfolio.py](../apprentice_system/portfolio.py) · [risk.py](../apprentice_system/risk.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 4 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Gross/net exposure confusion; hidden beta despite dollar neutrality; alpha horizons inconsistent with holding policy; infeasible bounds; silent solver failure; target weights mistaken for realized exposures; costs proportional to total weights rather than changes.

## Debugging exercise

Make every alpha zero, make one alpha very large, and perturb forecasts slightly. Test whether allocation stays finite, feasible and proportionate. Construct a cap-and-renormalize counterexample and identify which postcondition fails.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose rank weighting, capped conviction or a constrained optimizer for noisy estimates. Write what the optimizer adds and what happens when its solution is unstable before reading the expert guidance.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Explicit objective/constraints; current-to-target order accounting; sensitivity report; cost/turnover comparison; handling of no signal and infeasible requests; no claims of beta neutrality without measured exposures.

## Deeper teaching and existing worked projects

[14 risk forecasts](../lessons/14_risk_forecasts.md) · [15 portfolios](../lessons/15_portfolios.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/04_economic_value.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
