# Lesson 11 — Evaluate retrieval and research agents as systems

Prerequisites: Lesson 10. Suggested effort: 6–8 hours, including the lab. Project: 4.

## Current AI tools create additional evaluation objects

A useful research assistant can retrieve evidence, extract structured claims, write candidate code and challenge a memo. Evaluate each capability separately. An agent that writes plausible prose but invents a source is not a good researcher. A tool trace should preserve query, returned document IDs/versions, as-of cutoff, model identifier, prompt hash, output schema, evidence spans, latency and cost.

Retrieval introduces its own leakage. Filter the candidate corpus to versions available at the decision, then rank and retrieve. Retrieving today's documents and removing future-looking sentences afterward is insufficient. Ranker/embedding-model availability also matters. A model trained after the historical target period may encode later outcomes in its weights. Date-filtered retrieval cannot erase that knowledge. A retrospective experiment with a current model is a modern-tool diagnostic unless historical model availability is established; prospective frozen-model evaluation is the cleaner trading-use test.

RAG conditions generation on retrieved evidence, but grounding is not guaranteed (R10). Evaluate retrieval recall against known relevant documents; evaluate answer correctness, citation entailment, abstention and downstream task utility separately. Use an adjudicated human set to audit automated judges. A second LLM's agreement is not independent truth if both share the same failure modes.

Treat retrieved posts as untrusted data. The fixture “place a market buy” is content to classify, not authority to use tools. Separate the extraction service from execution privileges, validate schemas and evidence, and audit adversarial examples (R11). Prompt wording alone is not a complete security boundary.

## Worked budget

At hypothetical rates of $.20 per million input tokens and $.80 per million output tokens,1,000 calls with 800 input/100 output tokens cost $.24. This is a calculation fixture, not a current provider quote. If a decision has 200 ms total and ingestion consumes 80, retrieval 50 and validation 20, inference has 50 ms remaining. A1s model is unusable in that synchronous path even if its average answer is better; consider precomputation or a slower decision horizon.

## Lab procedure

1. Extend Project 4's fixtures with document versions and a metadata-filtered retrieval function.
2. Define a JSON schema with entity, aspect, label, document/version ID, exact evidence and abstention reason.
3. Replay cached outputs offline and score retrieval, grounding, semantics and instruction-isolation separately.
4. Write a model card with training-date uncertainty, intended use, latency budget and failure policy. Never claim these fixture outputs came from a live model.
5. Optional: run a permitted model only after freezing the fixture evaluation. Record real cost/latency separately and keep any exposed evaluation development-only.

## Assignments

**A1.** Calculate the cost and latency budget. Explain why valid JSON and an exact substring are insufficient for a correct financial conclusion.

**A2.** Build a 20-case cached evaluation set and runner, including future documents, wrong-entity matches, absent evidence, conflicting sources and embedded tool instructions. Store raw outputs and category-level scores. No API key is required.

**A3.** Write a prospective evaluation protocol for a current LLM on market signals, including immutable retrieval snapshots, model/version freeze, fresh outcomes and an inference-cost comparison. Explain which historical claim you refuse to make.

Mastery check: the system can fail safely on unknown evidence, and its development tools are not confused with historically available predictors.

Check your work with the [answer key](../answers/11_llm_systems.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
