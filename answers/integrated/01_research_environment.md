# Hints and review guidance — Module 01

## Hint 1

Calculate payoff expectation before subtracting costs. A probability is not a payoff magnitude.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

0.55×8 − 0.45×12 − 3 = −4 bps. The direction is more likely up, but the stated long trade has negative expected net return. This does not establish that a short is feasible or attractive; its execution and financing would need a separate specification.

## Debugging guidance

The essential expected evidence is: A research contract, requirements sketch, reproducible command, manifest, independent numerical check and a short claim/limitation memo. Positive P&L is not required.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
