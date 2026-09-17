# Hints and review guidance — Module 05

## Hint 1

Either compare cash plus inventory, or use carry plus signed trade-to-mark minus fees.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

Carry = 10×(49−50)=−10. Trade-to-mark = −4×(49−51)=+8. Fees = 2. Total = −4 dollars. Independently, sales add 202 cash and ending inventory is 294 versus initial inventory 500: 202+294−500=−4.

## Debugging guidance

The essential expected evidence is: Reconciled daily P&L; explicit costs/cashflows; exposure and scenario reports; named residual limitations; one failure postmortem; no unexplained accounting residual.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
