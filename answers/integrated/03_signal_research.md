# Hints and review guidance — Module 03

## Hint 1

Ask what information each fitted object and label contains, not just when its row begins.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

The scaler leaks evaluation-distribution information; fit it on training data within each split. The unmatured label is ineligible. Correcting either issue alone does not repair the other. Repeatedly tuned evaluation dates also become development evidence.

## Debugging guidance

The essential expected evidence is: Frozen hypothesis and variant ledger; matched baseline comparison; chronological split diagram; leakage mutation test; uncertainty interpretation; a negative-result decision as defensible as a positive one.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
