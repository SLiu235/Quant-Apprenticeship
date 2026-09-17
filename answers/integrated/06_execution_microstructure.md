# Hints and review guidance — Module 06

## Hint 1

A request does not erase remaining exposure. The same event must have the same effect once.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

Forty shares remain to cancel. Final totals are 40 filled and 40 cancelled. An identical repeated fill ID has no additional effect; the same ID with conflicting contents must raise an integrity failure. This does not imply that receiving a broker fill can simply be rejected economically; live recovery must reconcile what actually occurred.

## Debugging guidance

The essential expected evidence is: Order conservation; buy/sell cost checks; explicit fill assumptions; delay/spread/impact/fees/opportunity decomposition; cost sensitivity; queue and cancel-race tests; a no-trade case.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
