# Lesson 19 — Make an experiment independently reproducible

Prerequisites: Lessons 1–18. Suggested effort: 5–7 hours, including the lab. Project: 7.

## Reproducibility is a dependency claim

A result depends on code, data, configuration, environment, model artifacts and runtime behavior. A notebook with a fixed random seed does not capture all of these. Preserve raw snapshot hashes, feature/label schema, splits, candidate ledger, fitted transformations, software versions and commands. An experiment ID should name immutable inputs; rerunning a changed file under the same label conceals a different experiment.

Keep pure numerical transformations separate from I/O and stateful effects. A pure scoring function can be checked against hand arithmetic; an execution reducer can replay an event log. Tests should enforce economic and temporal invariants, not merely assert that a function returns the value hardcoded inside it. Use an independent formula, conservation law or adversarial input as an oracle.

Useful invariants include probabilities sum to 1; feature availability precedes decisions; training labels have arrived; cash/share accounting conserves value under a split; repeated fill IDs do not duplicate cash; covariance is symmetric; constraints hold; impossible actions have zero probability. Future-perturbation tests detect accidental dependencies that ordinary random train/test tests often miss.

## Worked incident in research

Two analysts report different NLLs. They first compare prediction-file hashes, episode IDs/class order, metric convention and date weights. If bytes match but scores differ, inspect arithmetic. If hashes differ, resolve data/model lineage before debating statistics. A source hash proves byte identity, not source truth, valid availability or an adequate population.

AI coding assistants can generate useful scaffolding and tests, but their assertions may mirror the same implementation mistake. Ask for independent failure cases and derivations, inspect the diff and execute checks yourself. Never treat an agent's “tests passed” sentence as evidence without the actual command and result.

## Lab procedure

1. Run all eight reference programs from a fresh Python process, preserving the recorded outputs in a separate directory if comparing.
2. Write a manifest with input hashes, versions, commands and output identities. Mark timing fields nondeterministic.
3. Add tests that intentionally mutate a future value, duplicate a fill and swap class columns.
4. Ask a peer or a separate review pass to reproduce one result using only the README. Record every missing instruction as a defect.
5. Read R2 for pipeline consistency. Inspect the local test suite to see how statistical and economic checks differ.

## Assignments

**A1.** Explain why matching seeds is insufficient and why matching hashes is insufficient for validity. Give one failure of each.

**A2.** Package your Project 3 or Project 6 submission with a single run command, environment record, manifest, tests and memo. Re-run into a new output directory and compare deterministic fields.

**A3.** Write a review of a hypothetical AI-generated test that calls `metric(x)` to create the expected result and then asserts `metric(x)` equals it. Replace it with two meaningful checks.

Mastery check: another researcher can reproduce your evidence without your shell history or hidden notebook state.

Check your work with the [answer key](../answers/19_research_software.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
