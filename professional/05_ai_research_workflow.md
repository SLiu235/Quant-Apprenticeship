# Research studio — Accountable AI-assisted research

[Professional track](../PROFESSIONAL_TRACK.md) · [Evidence rubric](../assessments/PROFESSIONAL_EVIDENCE.md)

## Objective and prerequisites

Use AI to improve the quality or efficiency of research while retaining responsibility for evidence, code, model selection and tool effects.

Enter from Modules 7–8. This is self-paced project work. You are not being assessed by reading it.

## Core knowledge

Split AI tasks into evidence retrieval, structured extraction, code generation, hypothesis generation and experiment interpretation. They need different evaluations. A citation can be exact while an interpretation is wrong. Valid JSON is a format property. A second model can share the same blind spot. Use adjudicated cases, independent numeric checks and human review where the consequence requires it.

Historical availability has two layers: source documents and the model itself. Date-filtering retrieval does not remove knowledge encoded during pretraining. Store model/version, claimed training cutoff, availability, prompt, corpus snapshot and tool trace. Unknown provenance limits the claim; prospective frozen-model evaluation is a way to collect cleaner evidence, not a promise of future profit.

For AI-assisted code, record the task, proposed change, tests, rejected alternatives and your reasoning. Treat prompts and generated features as research variants when they influence selection. Measure time to a verified result, error rate and review burden, not generated lines of code. Retrieval text cannot grant execution permission. Tool boundaries belong in the application design, not just the prompt.

## Mental model

AI is a powerful research instrument whose output remains your responsibility. The competitive skill is asking discriminating questions and verifying the answer economically and technically.

## Worked case

The authored evaluation fixture has 100% quotation support among answered cases, but only 50% selective accuracy. One answer cites genuine text while missing a negative qualification. Evidence support and semantic correctness must be measured separately.

## Implementation project

Create a minimum 20-case task-specific evaluation with normal, ambiguous, future-dated, unsupported, wrong-entity and instruction-bearing examples. Score structured outputs with the supplied evaluator. Run a real model only with available authorized access, record actual resources, and label authored/cached/live outputs correctly. Compare against deterministic retrieval and a reviewed manual baseline.

Save independent work under `submissions/professional/05_ai_research_workflow/`. Before coding, define requirements, data contracts, assumptions, alternatives and failure detection. Use the [research agenda](../templates/professional/research_agenda.md), [experiment protocol](../templates/professional/experiment_protocol.md), [edge/data card](../templates/professional/edge_data_card.md) and [committee memo](../templates/professional/committee_memo.md) where relevant.

## Failure cases

Calling hand-written fixtures model results; stripping dates without addressing weight contamination; accepting AI-generated tests that merely encode the same bug; measuring speed without verification time; allowing document content to issue orders.

## Debugging exercise

An AI-generated function passes its generated tests but fails a hand-reconciled P&L fixture. Trace the shared assumption. Add an independent invariant test and document whether the interface made the error easy to introduce.

Preserve symptom, competing hypotheses, discriminating evidence, earliest violated invariant, root cause, fix and regression test. Ask for progressively stronger hints if stuck.

## Decision exercise

Choose a deterministic workflow, one model call or an agent for a research task. Identify the capability requiring planning and the failure budget before increasing autonomy.

Write your decision before consulting the reference or requesting the mentor's tradeoff analysis.

## Completion evidence

Frozen task/evaluation set; output provenance; semantic/evidence/abstention measures; actual cost/latency if live calls occur; contamination review; permission boundaries; independent audit of AI-generated code; a measured decision on whether AI adds value.

Attach evidence for each claim. Missing evidence remains unverified rather than filled with a confident narrative. A meaningful negative result can meet the research objective. Source-code execution alone cannot.

## Optional self-assessment

One assistant completes a task in 2 minutes but requires 20 minutes of verification. Another takes 8 minutes and needs 3 minutes of review. Which is more productive under the stated workflow?

<details>
<summary>Open a hint or answer only when you choose</summary>

The verified totals are 22 and 11 minutes. Include error cost, recurrence and quality before generalizing. A faster initial answer need not create a faster trustworthy result.

</details>

For mentor review, submit the original attempt, relevant code/data manifest, failure investigation and decision memo. Review will identify what is correct, questionable and wrong, then assumptions and next investigations; it will not automatically replace your work or promote your level.
