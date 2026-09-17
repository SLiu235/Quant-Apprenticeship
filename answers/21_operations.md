# Lesson 21 answer key — Operate a paper research system and recover from failures

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Cash 10,000−15×100−25×100.04=5,999; shares 40; midpoint equity 5,999+40×100.02=9,999.80. Duplicate processing would wrongly subtract another 1,500 and add 15 shares. New-order halt must still process valid authoritative fills and cancel reports so exposures remain accurate.

## A2

Reference tests cover duplicates, stale quotes, overfills and reconciliation. Your journal extension persists event ID, payload, sequence and application status; reconstruction must deduplicate across process boundaries, not just in an in-memory set. Append/checkpoint ordering must ensure a crash cannot lose an applied fill or apply it twice. Accept a simple local write-ahead journal with explicit fsync/atomic-checkpoint assumptions and crash fixtures; do not call it production-ready without testing those assumptions.

Expected scenario: replay the trace twice from durable events yields cash 5,999/shares 40 once, not doubled. An overfill leaves financial state unchanged and halts. A mismatch blocks resume until reconciliation and operator/data conditions pass. An operator flag alone is insufficient.

## A3

First inspect ingestion status, receipt lag, provider responses, schema and predetermined coverage by session. Compare expected activity against independently observed source availability and historical session patterns. If feed failure is plausible, suppress affected decisions rather than interpreting zeros as sentiment. Model drift needs valid inputs and subsequently available labels. Retraining during an outage learns the outage. Resume requires restored/understood coverage, replay/reconciliation and applicable session/risk checks.

Repair: simulate a valid late fill while halted. If your system discards it, repair operations before any deployment discussion.
