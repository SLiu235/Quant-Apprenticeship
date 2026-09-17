# Hints and review guidance — Module 04

## Hint 1

Compute target shares from decision-time inputs; then distinguish a target from the realized portfolio.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

Target shares = 200000×0.15/40 = 750; order = +150 shares. The final weight is not necessarily 15% because execution price, fees, other assets and the equity mark affect the realized denominator and numerator. Reconcile cash and mark the full portfolio.

## Debugging guidance

The essential expected evidence is: Explicit objective/constraints; current-to-target order accounting; sensitivity report; cost/turnover comparison; handling of no signal and infeasible requests; no claims of beta neutrality without measured exposures.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
