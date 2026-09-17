# Project 4 — Build an auditable AI evidence pipeline

Lessons: 10–12. Integration effort after lessons: 12–20 hours. Workspace connection: sentiment_pipeline and QuantKG.

## Research question and input

Can a text-processing system produce valid, grounded, temporally eligible features, and how would we test their incremental value? The required reference has author-written text and deliberately imperfect simulated cached outputs. Its small accuracy is a software fixture result, not a measured LLM benchmark. It separately links to the real frozen public-versus-market forecast audit.

## Build it step by step

1. Write annotation rules for entity, aspect, quotation, polarity/mixedness and abstention.
2. Prepare a 20-case cached evaluation set, including the six reference cases plus your own adversarial cases. Label it before inspecting candidate outputs.
3. Filter versioned documents by actual/assumed availability before retrieval. Record the distinction and preserve evidence IDs.
4. Validate schema and exact evidence, then separately assess semantic faithfulness with gold annotations. Track abstention and coverage.
5. Keep retrieved instructions powerless: the extraction component has no trading or message-sending tools.
6. Design a matched market/lexical/encoder comparison and typed temporal-graph ablations. Do not claim this fixture runner trained or evaluated a live LLM.

## Student deliverables

Annotation guide, versioned fixture set, cached raw outputs, evaluation runner, confusion/coverage/error tables, model card, hypothetical versus measured cost ledger and prospective market-evaluation protocol. Include model-date contamination and graph-edge semantics.

## Worked project and interpretation

Five reference documents are eligible at cutoff; one future document is excluded. Four outputs pass a simple evidence check; three are nonabstentions. Accepted accuracy is 2/3 at 60% coverage. One exact quote supports only part of a mixed statement, so it passes grounding while failing interpretation. One invented quote is rejected. An embedded instruction to trade is treated as untrusted text.

The real saved text feature worsens the market baseline; the synthetic extraction cases do not overturn that result. A sample decision is to repair measurement/evaluation first, then test a frozen representation prospectively if acquisition is justified. A current model's performance on old events is not proof that the model could have been deployed then.

## Acceptance and answer guidance

Reject future versions before ranking, preserve unknown coverage and distinguish validity/grounding/semantics/downstream value. All raw failures must remain inspectable. Keys 10–12 provide the expected reference counts and causal/temporal reasoning. For your new fixtures, gold labels may be debated; resolve ambiguity before using them as an evaluation standard.

Optional model upgrade: evaluate a local or authorized API model with version, prompts, real latency and costs recorded. Use frozen cases and a separate human-adjudicated subset; do not let an LLM judge become the only source of truth. Any new evaluation inspected during development must be treated accordingly.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 4
```

[Complete reference code](../reference/p04_text.py) · [Recorded result](../outputs/p04_text.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
