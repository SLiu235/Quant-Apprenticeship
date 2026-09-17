# Module 08 — AI research assistant and knowledge system

[Full package](../FULL_PACKAGE.md) · [Project](../projects/integrated/08_ai_research_copilot.md) · [Optional assessment](../assessments/integrated/08_ai_research_copilot.md)

## Objective

Build an evidence-grounded research assistant and determine whether an AI model adds measurable value over retrieval.

## Prerequisites and pace

Point-in-time provenance, research evaluation and versioned artifacts. Work at your own pace. Reading and experimenting do not trigger an assessment. Completion criteria describe evidence to work toward; review occurs when you request it, submit work, or when a serious error blocks a dependent milestone.

## Core knowledge

Separate retrieval quality, evidence fidelity and decision usefulness. Temporal filtering precedes retrieval. A valid citation must resolve to eligible source evidence; substring matching alone does not prove the interpretation is faithful. Retrieval coverage and selective accuracy must be reported together so abstaining on everything cannot look successful. Documents are untrusted data. The integrated code returns quoted evidence and cannot issue orders; a future generator must preserve that tool boundary and be evaluated on malicious and unsupported inputs.

## Mental models

The assistant proposes or retrieves evidence; the research process owns the claim. Start with a deterministic baseline and make every added model earn its cost, latency and failure burden. A fluent answer is not an audit trail.

## Worked example

A query asks about execution costs at a 2025 cutoff. A 2030 policy must be excluded even if its wording matches perfectly. If no eligible source supports the query, return an explicit abstention. A real quotation can still be irrelevant or omit a crucial qualification.

## Implementation

Run the lexical retrieval baseline and citation checks. Create an evaluation set with expected sources, unsupported questions, stale documents and hostile text. Then add a model adapter if you have a provider and compare against the same frozen set.

Read the contracts and trace one observation before editing. Reference code: [copilot.py](../apprentice_system/copilot.py).

From the package directory, run this stage and its prerequisites:

```bash
python3 -m apprentice_system.run --stage 8 --output outputs/integrated
```

The reference uses Python's standard library. Each report is `outputs/integrated/stage_XX.json`; stage 2 also saves its synthetic input fixture. Python 3.11 or newer is the supported baseline.

## Failure cases

Future documents; invented source IDs; correct quote with false paraphrase; corpus used as instructions; retrieval test leakage; unmeasured abstention; model silently changing versions; an agent with trading permissions unrelated to its research task.

## Debugging exercise

Trace a bad answer through query, cutoff, retrieved documents, reranking, generation and validation. Identify the first unsupported claim. Inject a fabricated quote and an instruction-bearing document. A lexical match should never become authority to execute a tool.

Write symptom → hypotheses → evidence → earliest failing invariant → root cause → fix → regression test. Inspect the reference only after trying to isolate the failure. Do not change raw evidence to make expected numbers match.

## Decision exercise

Choose deterministic search, embeddings plus reranking, RAG or an agent. Identify the additional task each component enables and the fixed evaluation it must improve before selecting it.

Make your decision first. Record alternatives, assumptions, expected outcome and what would make you reconsider in the [decision journal](../records/decision_journal.md). Expert reasoning is available in the linked lessons and optional answer key.

## Completion criteria

Frozen evidence set; temporal retrieval tests; citation and semantic review; abstention coverage; injection cases; versioned outputs; measured cost/latency for any real model calls.

## Deeper teaching and existing worked projects

[10 text features](../lessons/10_text_features.md) · [11 llm systems](../lessons/11_llm_systems.md) · [12 graphs causality](../lessons/12_graphs_causality.md)

The [full index](../FULL_PACKAGE.md) maps the existing empirical, execution, AI and RL projects to this integrated backbone. See [source and scope notes](../guides/INTEGRATED_SCOPE.md) for the boundary between runnable reference functionality and project extensions.

## Professional research deliverable

This foundation now feeds [the professional research studio](../professional/05_ai_research_workflow.md). Use it to investigate an independently stated investment problem, preserve the search and failures, and explain what evidence changes the decision. The [professional track](../PROFESSIONAL_TRACK.md) supplies the stronger evidence requirements and new executable labs. No automatic assessment is triggered.
