# Project 2 — Reconstruct a market decision and order lifecycle

Lessons: 04–06. Integration effort after lessons: 10–16 hours. Workspace connection: ExecutionLab and BehaviorIRL session controls.

## Research question and input

What can an execution policy actually observe, request and fill? The required core uses a stipulated synthetic FIFO event sequence so every quantity has an independently checkable answer. It does not use historical exchange orders. Read the ITCH specification for a future parser design, but do not imply that our small reducer implements the exchange.

## Build it step by step

1. Complete instrument/cashflow arithmetic and decide the price, fee and quantity units.
2. Implement a passive-order reducer with queue-ahead, own remaining quantity and partial fills.
3. Reproduce the 40-share scenario, then add a cancel request followed by an intervening fill and later acknowledgment.
4. Add event IDs, sequence-gap handling and invalid/duplicate-event tests. Track cash and shares from fills.
5. Add a separate synthetic session calendar with holidays, daylight-time conversion and reset behavior. Store the rules version.
6. Produce a timeline of feed receipt, policy completion, order request/acknowledgment and fill reports. Stipulated latencies must be labeled assumptions.

## Student deliverables

`replay.py`, an event fixture, order/cash state traces, `calendar_rules.json`, tests and a research memo. Explain whether the output is a counterfactual fill assumption or an observed execution. Include unfilled quantities in the evaluation.

## Worked project and interpretation

The reference has 40 shares ahead and a 40-share passive buy at 100.00. Trades 25 and 30 fill 15 of our shares. Canceling the remaining 25 and buying at 100.04 produces VWAP 100.025. Fees are $.16 and arrival-midpoint shortfall is $.36, about .89982 bps. Changing only the aggressive price to 100.10 raises shortfall to $1.86. This sensitivity shows why a cheap partial fill is not enough to evaluate a complete mandate.

The sample memo would recommend using the reducer for accounting tests and rejecting its use as a calibrated Nasdaq fill simulator. Hidden liquidity, routing, cancel races and impact are omitted. A stronger empirical project needs actual order/receipt/fill histories and a declared queue estimator.

## Acceptance and answer guidance

Cash/share conservation and filled +canceled +remaining=requested must hold after every valid event. Duplicate IDs must be idempotent; an overfill must not change balances. A cancel request cannot zero exposure before acknowledgment. Calendar tests must include an explicitly synthetic holiday and winter/summer offsets. Keys 04–06 provide the worked amounts and expected edge cases.

Optional data upgrade: parse a licensed, versioned small ITCH slice and validate message counts, sequence continuity and book reconstruction against an independent reference. A venue order ID is not permission to claim a named investor's inventory or intention.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 2
```

[Complete reference code](../reference/p02_replay.py) · [Recorded result](../outputs/p02_replay.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
