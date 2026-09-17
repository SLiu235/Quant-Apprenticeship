# Research studio — Predictive AI and representation research

[Professional track](../PROFESSIONAL_TRACK.md) · [Evidence rubric](../assessments/PROFESSIONAL_EVIDENCE.md)

## Objective and prerequisites

Build and diagnose actual predictive models, then identify whether their incremental value comes from representation, optimization, data or selection.

Enter from Modules 3 and 7. This is self-paced project work. You are not being assessed by reading it.

## Core knowledge

The model is more than its architecture name. Specify inputs, target, loss, normalization, missingness, sampling, training budget, checkpoint rule and inference path. Start with a mathematical objective and a tiny forward/backward example. Learn enough of the implementation to distinguish a bad gradient from poor conditioning or an uninformative target.

The runnable lab compares zero, ridge, ablated ridge and two genuinely trained small MLPs. It uses training-only feature/target scaling and validation-only MLP checkpoint selection. That is an operational example of nonlinear modeling, not a demonstration of frontier model capability. A more advanced project must earn its representation: a causal sequence encoder for sequential information, an event representation for irregular data, or a text model for measured semantic information.

Compare learning curves by data quantity as well as epochs. Report seed sensitivity and compute/time measurements under a predeclared budget; do not pick the most flattering seed. Check calibration on a separate appropriate sample before turning a residual scale into confidence. Under distribution shift, test what changes in inputs, labels and decision utility rather than giving every failure the name regime change.

## Mental model

Complexity is a research instrument. A simple model can expose inadequate data; a deep model can reveal interactions a linear baseline cannot represent. Both need a fair experiment.

## Worked case

An MLP improves training loss but worsens validation loss. Before adding layers, inspect leakage, target alignment, learning-rate stability, sample size and regularization. If all models fail similarly on a shifted sample, more optimization may be addressing the wrong problem.

## Implementation project

Run the five-model lab and reproduce one prediction from saved parameters. Extend with one justified representation and two diagnostic ablations under a fixed compute budget. Save checkpoint, training curves, parameter count and inference contract. Validate gradients or use an independently tested autograd path. Profile memory/latency before proposing GPU or distributed changes.

Save independent work under `submissions/professional/03_predictive_ai/`. Before coding, define requirements, data contracts, assumptions, alternatives and failure detection. Use the [research agenda](../templates/professional/research_agenda.md), [experiment protocol](../templates/professional/experiment_protocol.md), [edge/data card](../templates/professional/edge_data_card.md) and [committee memo](../templates/professional/committee_memo.md) where relevant.

## Failure cases

Future-aware normalization; encoder weights pretrained beyond the claimed historical decision; best-seed reporting; comparing different populations; a model card without actual parameter lineage; generalizing from one chosen architecture to all neural models.

## Debugging exercise

Multiply evaluation labels by −100 in a copied fixture. Training parameters, selected model and predictions must not change. Then intentionally change a training normalization step and locate the earliest altered tensor.

Preserve symptom, competing hypotheses, discriminating evidence, earliest violated invariant, root cause, fix and regression test. Ask for progressively stronger hints if stuck.

## Decision exercise

Your nonlinear model beats ridge by a small amount but uses much more compute and is unstable across liquidity regimes. Decide whether to deploy a research prototype, collect more data, simplify or reject it. Explain what economic difference the metric improvement could make.

Write your decision before consulting the reference or requesting the mentor's tradeoff analysis.

## Completion evidence

Actual trained models; reproducible parameters; matched baseline and ablation; training diagnosis; future-data mutation check; measured resources; uncertainty/shift analysis; an explicit representation decision.

Attach evidence for each claim. Missing evidence remains unverified rather than filled with a confident narrative. A meaningful negative result can meet the research objective. Source-code execution alone cannot.

## Optional self-assessment

A model wins only after selecting the best of 30 seeds. Another model is stable over the same seeds. What deployment procedure are you really comparing?

<details>
<summary>Open a hint or answer only when you choose</summary>

Compare the declared seed-selection or ensemble procedure, not a lucky realization. Final evaluation must test that procedure, including its computational cost and validation choices.

</details>

For mentor review, submit the original attempt, relevant code/data manifest, failure investigation and decision memo. Review will identify what is correct, questionable and wrong, then assumptions and next investigations; it will not automatically replace your work or promote your level.
