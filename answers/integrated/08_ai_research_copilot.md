# Hints and review guidance — Module 08

## Hint 1

The denominator for coverage differs from the denominator for accuracy on answered questions.

## Hint 2

Return to the module's worked example and explicitly label clocks, units and the decision being made. Write the invariant before inspecting the implementation.

## Part A answer

A: coverage 40%, selective accuracy 95%. B: coverage 90%, selective accuracy 80%. There is no automatic winner without the cost of wrong answers, value of coverage and review capacity. Verify that abstention policy was not tuned on the final evaluation cases.

## Debugging guidance

The essential expected evidence is: Frozen evidence set; temporal retrieval tests; citation and semantic review; abstention coverage; injection cases; versioned outputs; measured cost/latency for any real model calls.

Begin with the smallest failing input. Record the first incorrect intermediate value and identify which assumption allowed it. A code change without a reproducer or a causal explanation is incomplete. The reference tests under `tests/test_integrated.py` illustrate a supported subset; the project extension needs its own targeted checks.

## Decision review

A defensible response ties the choice to the stated requirements, uncertainty and cost of failure. Complexity earns its place only when the simple alternative fails a relevant requirement or measured evaluation. There is no universal preferred database, optimizer, model or execution style. Explain which additional evidence changes your decision.

## Review protocol

Identify what is correct, questionable and wrong; enumerate assumptions; propose the next investigation before rewriting code. Preserve the learner's original answer. No score here automatically changes the Skill Gap Ledger or confers a competency level.
