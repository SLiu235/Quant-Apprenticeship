# Project 7 — Build a measurable and recoverable paper research service

Lessons: 19–21. Integration effort after lessons: 12–20 hours. Workspace connection: ExecutionLab and QuantCUDA.

## Research question and input

Can the research code produce correct decisions within a measured budget and maintain accounting through failure? The reference uses synthetic events and actual local CPU timings. It has no broker, trading account, network side effect or GPU result.

## Build it step by step

1. Package one prior project with configuration, source/output hashes, versions and a single command.
2. Profile the full workload. Benchmark a measured numerical bottleneck against a CPU reference with warm-up and repeats.
3. Validate numeric agreement and downstream threshold decisions before discussing speedup.
4. Implement a paper state machine for submission, fill, halt, reconciliation and resume. Continue processing valid fills while halted.
5. Add a single-writer durable journal and replay from genesis or a verified checkpoint. Test duplicate IDs across restart and corrupted trailing records.
6. Write an incident runbook and execute an outage/drift exercise. Keep market rules and risk policy explicit.

## Student deliverables

Runnable package, benchmark protocol/results, fault-injection tests, event journal/replay code, state trace, incident report and resource budget. The operational scope must list implemented controls and omissions so a reviewer cannot mistake the teaching reducer for a production OMS.

## Worked project and interpretation

The reference applies 15 and 25-share fills once each, ignores an exact duplicate, halts on a stale quote and still reconciles the later fill. It refuses resume before reconciliation and then resumes under the declared operator/freshness policy. Final cash is $5,999, shares 40, midpoint equity$9,999.80 before fees.

The benchmark compares Python looping with NumPy multiplication on 4000×16 inputs, recording seven repeats and numeric disagreement. Timing varies across runs and hosts; no universal speedup is asserted. This workload illustrates vectorization and independent correctness, not low-latency market connectivity.

## Acceptance and answer guidance

Duplicate events cannot double cash effects. Invalid overfills cannot mutate accepted financial state. An unmatched broker state blocks resume. The journal must detect conflicting duplicate IDs or corruption; explicit repair is preferable to silently discarding an unknown financial event. Keys 19–21 and `reference/solutions.py` give a complete small write-ahead/replay example with stated crash assumptions.

Extension: benchmark a GPU only if available and a measured workload justifies it; include transfers, synchronization, versions and decision correctness. Production deployment would require additional venue/broker integrations, durable-state guarantees, cash/short controls, operational review and authorization; none is claimed by this lab.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 7
```

[Complete reference code](../reference/p07_operations.py) · [Recorded result](../outputs/p07_operations.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
