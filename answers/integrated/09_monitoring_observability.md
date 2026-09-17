# Hints and review guidance — Module 09

## Hint 1

Freshness checks need a lower as well as an upper age bound. Pausing intent does not erase economic events.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

No: negative quote age indicates a clock/timestamp problem and requires investigation. Genuine fills must still be captured and reconciled while new orders are paused. Recovery requires trustworthy state and a defined resume decision, not merely the disappearance of the alert.

## Debugging guidance

The essential expected evidence is: Actionable alert catalog; freshness/NaN/reconciliation tests; incident timeline; restart/resume criteria; concise postmortem; clear separation between operational failure and investment underperformance.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
