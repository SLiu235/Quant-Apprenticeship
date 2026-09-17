# Hints and review guidance — Module 10

## Hint 1

Separate software invariants from empirical identification and feasibility.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

It supports the tested simulation behavior, not investability. Next evidence includes point-in-time empirical inputs, frozen prospective evaluation, feasible costs/liquidity and independently reconciled execution assumptions. Forecast/holding horizon mismatch, missing terminal liquidation, selection bias or unmodeled costs can make an economically misleading result despite passing tests.

## Debugging guidance

The essential expected evidence is: One-command replay; reconciled event history; matched baselines; horizon-consistent accounting or an explicit attribution split; stress/cost sensitivity; incident recovery evidence; committee memo and an honest skills-gap update. No automatic promotion or capital deployment.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
