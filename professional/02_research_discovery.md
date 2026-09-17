# Research studio — Replication, falsification and original research

[Professional track](../PROFESSIONAL_TRACK.md) · [Evidence rubric](../assessments/PROFESSIONAL_EVIDENCE.md)

## Objective and prerequisites

Replicate an empirical result, design a meaningful extension and show that the search itself has not manufactured the evidence.

Enter from Modules 2–3. This is self-paced project work. You are not being assessed by reading it.

## Core knowledge

Reproduction reruns an existing procedure; replication independently checks its claim with a defensible implementation or sample; an original extension changes an identified limitation or poses a new question. They are different deliverables. A supplied reference result is a useful starting point, not your original contribution.

Reserve trials before computation. Count feature variants, labels, data filters, seeds, prompts and checkpoints under the declared selection procedure. Failures consume resources and belong in the record. Freeze the chosen procedure before evaluating it. In adaptive walk-forward research, scheduled refits may use newly matured labels if that procedure was specified in advance; arbitrary adaptation after seeing losses is different.

Design controls that could falsify the proposed explanation. Examples include a price-only baseline, feature ablation, a clock-delay sensitivity and a within-date randomized placebo whose permutation preserves the relevant sampling structure. A placebo must be chosen with the dependence and economic hypothesis in mind. A block interval quantifies uncertainty under its assumptions; it does not repair undisclosed search.

## Mental model

A useful experiment can teach you that an idea is wrong. Replication is an exercise in locating fragile assumptions, not matching a printed number at any cost.

## Worked case

The supplied real-data model lab selects an MLP on validation, but the selected model fails to beat zero on the inspected final block. Choosing a different model after reading that block starts a new development decision; it cannot be relabeled an untouched test.

## Implementation project

Independently reproduce the existing public-signal audit or a primary-paper result with accessible data. Commit a protocol through ExperimentBook. Add exactly one economically motivated extension, one baseline and one diagnostic control. Reserve an explicit trial budget and preserve failed attempts. Compare equally weighted dates on identical populations.

Save independent work under `submissions/professional/02_research_discovery/`. Before coding, define requirements, data contracts, assumptions, alternatives and failure detection. Use the [research agenda](../templates/professional/research_agenda.md), [experiment protocol](../templates/professional/experiment_protocol.md), [edge/data card](../templates/professional/edge_data_card.md) and [committee memo](../templates/professional/committee_memo.md) where relevant.

## Failure cases

Reporting only successful trials; treating a rerun as independent evidence; interpreting a current snapshot as point-in-time data; claiming significance from the best of many unlogged results; calling inspected course data unseen.

## Debugging exercise

Reserve two trials and crash one before completion. Try to reserve a third under a two-trial budget. Then lock a completed candidate and try to overwrite its evaluation. Explain why these controls still cannot detect off-book experiments.

Preserve symptom, competing hypotheses, discriminating evidence, earliest violated invariant, root cause, fix and regression test. Ask for progressively stronger hints if stuck.

## Decision exercise

Your primary result is weak, but a subgroup looks excellent. Decide whether the subgroup analysis changes the main conclusion, supports a new hypothesis or justifies stopping. Record what data would be needed next.

Write your decision before consulting the reference or requesting the mentor's tradeoff analysis.

## Completion evidence

A replication report, one original extension, immutable protocol, all trial outcomes, justified controls and uncertainty, and a clear distinction between development and genuinely prospective evidence.

Attach evidence for each claim. Missing evidence remains unverified rather than filled with a confident narrative. A meaningful negative result can meet the research objective. Source-code execution alone cannot.

## Optional self-assessment

You generate 200 AI-suggested features but train only the five that look promising on the same data. How many stages of selection need to be disclosed?

<details>
<summary>Open a hint or answer only when you choose</summary>

Both feature screening and model fitting contributed to selection. Record the 200 proposals and the screen, not merely the five training runs. A budget is a research control, not a mathematical multiplicity correction.

</details>

For mentor review, submit the original attempt, relevant code/data manifest, failure investigation and decision memo. Review will identify what is correct, questionable and wrong, then assumptions and next investigations; it will not automatically replace your work or promote your level.
