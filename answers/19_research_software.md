# Lesson 19 answer key — Make an experiment independently reproducible

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

The same seed with different raw revisions, software kernels, thread reductions or candidate selection can produce different results. Matching bytes can reproduce leaked, selected or incorrectly labeled data perfectly. Reproducibility and validity are separate properties; both matter.

## A2

Required package: run command from a declared directory, dependency versions, source/feature/split IDs, seed, frozen settings, code/tests, outputs and interpretation. Compare forecasts/losses within declared numerical tolerances and record any solver variation. Do not compare CPU timings for exact equality. A missing paid source may make independent execution infeasible; include a redistributable fixture and label which empirical reproduction remains access-dependent rather than pretending it is bundled.

The course's own `reference.run`, recorded outputs and test log form one complete example. Your package must show your own artifact lineage, not simply point to the course file after changing data.

## A3

The test is tautological and cannot detect a shared implementation error. Replace with p=(.2,.3,.5), y=2, known NLL−ln(.5) and Brier.38, plus a permutation fixture showing that swapping the realized-class probability changes NLL as predicted. Another valid check rejects probabilities summing to 1.2. For a reducer, use independent cash conservation and idempotent duplicate-fill checks.

Repair: for every test, name the plausible bug it would catch. Remove or rewrite assertions that cannot answer this question.
