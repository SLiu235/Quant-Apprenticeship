# Integrated project 08 — AI research assistant and knowledge system

[Module notes](../../modules/08_ai_research_copilot.md) · [Optional self-assessment](../../assessments/integrated/08_ai_research_copilot.md)

## Problem and requirements

Build an evidence-grounded research assistant and determine whether an AI model adds measurable value over retrieval.

Use the shared synthetic fixtures and the component interfaces under `apprentice_system/`. The worked core already runs. Your independent project is the extension below, not copying the reference or rerunning its tests.

## Architecture before code

Write a one-page design covering requirements, scale/latency/cost constraints, data flow, component responsibilities, interfaces, failure detection, alternatives and tradeoffs. Compare at least two designs if you introduce a storage or service boundary. Choose the simplest design that satisfies the stated requirements.

## What to build

Implement an optional provider-neutral model adapter with structured answer fields, source IDs and abstention. Keep a replayable cache clearly labeled as cached. Evaluate retrieval recall and answer faithfulness separately. Add embeddings, GraphRAG or agents only after a measured retrieval/relationship/planning failure motivates them.

## Implementation sequence

1. Read the module and predict the hand-worked result before running code.
2. Create `submissions/integrated_08/`; keep your code and evidence there.
3. Define function inputs/outputs, units, clock semantics and error behavior.
4. Reproduce one happy path independently with a tiny fixture.
5. Implement the extension, then add the targeted failure fixture from the module.
6. Compare with the reference on its supported scope; document justified differences.
7. Write a decision memo: what is established, what is uncertain, and the next useful investigation.

## Required artifacts

corpus.json; eval_cases.json; retrieval report; model_adapter.py if used; answer schema; injection fixtures; model card; ablation/cost memo

## Acceptance evidence

Frozen evidence set; temporal retrieval tests; citation and semantic review; abstention coverage; injection cases; versioned outputs; measured cost/latency for any real model calls.

Assess correctness, research validity, simplicity, maintainability, reliability, performance, architecture and tests in that order. Keep the review focused on material issues. The optional [rubric](../../assessments/SELF_PACED.md) helps structure self-review; no automatic grading or promotion occurs.

## Failure to investigate

Trace a bad answer through query, cutoff, retrieved documents, reranking, generation and validation. Identify the first unsupported claim. Inject a fabricated quote and an instruction-bearing document. A lexical match should never become authority to execute a tool.

## Worked code and limitations

Reference source: `apprentice_system/copilot.py`. Run `python3 -m apprentice_system.run --stage 8` from the package directory. Reference limits are explicit in the module and [scope matrix](../../guides/INTEGRATED_SCOPE.md). Full independent extensions are deliberately your build tasks; the runnable core is supplied as a worked example.

## Professional extension

Complete the corresponding [research studio](../../professional/05_ai_research_workflow.md) when developing this component into professional research evidence. A reproduced reference and an original contribution are different deliverables. Record the distinction and connect the component to the investment decision.
