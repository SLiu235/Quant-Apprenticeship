# Hints and review guidance — Module 02

## Hint 1

The system cannot act on a publication it has not received. Apply the cutoff before selecting a revision.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

No: receipt is after the 12:02 decision. At 14:00 the initial received revision is eligible; the 15:00 correction is not. Real historical receipts may be unavailable, in which case label latency as an assumption and test sensitivity rather than claiming observed availability.

## Debugging guidance

The essential expected evidence is: An auditable as-of join; duplicate and schema checks; a future-revision invariance test; explicit missing-data and universe policies; lineage for one feature.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
