# Research studio — Edge and data advantage

[Professional track](../PROFESSIONAL_TRACK.md) · [Evidence rubric](../assessments/PROFESSIONAL_EVIDENCE.md)

## Objective and prerequisites

Choose a research problem whose resolution could change an investment decision, and explain why the available observations can address it.

Enter from Modules 1–2. This is self-paced project work. You are not being assessed by reading it.

## Core knowledge

Start with a market mechanism and the decision-maker who bears or supplies a risk. State the market-implied belief where it can be estimated, your competing forecast, why the difference might persist, and what observation separates your thesis from a conventional exposure. A story about a forced seller or a slow investor is a hypothesis, not proof of who trades.

Data advantage can come from coverage, timestamp quality, entity mapping, measurement, faster processing or a better model of the same information. A rare dataset is not automatically useful. Audit sampling, revisions, identifiers, units, availability and the limits of observation before fitting a model. Record source access and permitted uses; do not invent historical receipts or assume possession establishes redistribution rights.

Prioritize an experiment by its expected ability to change a decision relative to its time/data/compute cost. Estimate a range and name the uncertain assumption rather than pretending this priority score is precise.

## Mental model

The scarce resource is a good question with a discriminating observation. Ask what simpler explanation would make the apparent edge disappear.

## Worked case

A text feature predicts returns only in very small, illiquid names. Candidate explanations include new information, liquidity compensation, stale prices and selection. A test on comparable liquidity groups and feasible trading times is more informative than immediately replacing the text model.

## Implementation project

Choose one existing empirical study as context. Write three competing mechanisms, select one discriminating experiment, build a data card, and audit at least one row from source to feature. Compare two alternative sources or explicitly record why none is accessible. Do not buy data to complete the exercise.

Save independent work under `submissions/professional/01_edge_and_data/`. Before coding, define requirements, data contracts, assumptions, alternatives and failure detection. Use the [research agenda](../templates/professional/research_agenda.md), [experiment protocol](../templates/professional/experiment_protocol.md), [edge/data card](../templates/professional/edge_data_card.md) and [committee memo](../templates/professional/committee_memo.md) where relevant.

## Failure cases

An explanatory story stated as fact; a conveniently narrow population hidden in the conclusion; a dataset priced above its expected information value; publication time mistaken for system receipt; current identifiers applied to delisted or merged entities.

## Debugging exercise

A feature is absent for losing firms but populated for winners. Locate the first filtering/join rule that creates the difference; compare inclusion by outcome without using that analysis as a new trading signal.

Preserve symptom, competing hypotheses, discriminating evidence, earliest violated invariant, root cause, fix and regression test. Ask for progressively stronger hints if stuck.

## Decision exercise

Choose between acquiring another dataset, correcting the existing observation process and increasing model complexity. State the evidence that would reverse your priority.

Write your decision before consulting the reference or requesting the mentor's tradeoff analysis.

## Completion evidence

An edge card, competing explanations, one source-level availability audit, data diligence, an experiment priority memo and explicit kill criteria. At least one tempting idea should be rejected for a stated reason.

Attach evidence for each claim. Missing evidence remains unverified rather than filled with a confident narrative. A meaningful negative result can meet the research objective. Source-code execution alone cannot.

## Optional self-assessment

Your alternative-data signal adds 4 bps of expected gross return; execution and information delays could consume 2–8 bps. What additional evidence is valuable before sizing?

<details>
<summary>Open a hint or answer only when you choose</summary>

Distinguish uncertainty about gross prediction from uncertainty about feasibility. Investigate cost and timing jointly with the forecast horizon; a precise model of a non-executable opportunity is insufficient.

</details>

For mentor review, submit the original attempt, relevant code/data manifest, failure investigation and decision memo. Review will identify what is correct, questionable and wrong, then assumptions and next investigations; it will not automatically replace your work or promote your level.
