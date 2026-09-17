# Lesson 5 — Replay a decision and account for fills

Prerequisites: Lesson 4. Suggested effort: 5–7 hours, including the lab. Project: 2.

## The order lifecycle is part of the model

A limit order offers a price; it does not guarantee a fill. A marketable order consumes available liquidity and can receive several prices or fail under venue protections. Track request, acknowledgment, partial execution, cancel request, cancel acknowledgment and final state. A cancellation request does not erase exposure; fills may arrive while it is in flight.

A price-level book gives aggregate depth. Market-by-order messages can reveal displayed order lifecycles but still do not necessarily reveal hidden liquidity or a named investor's mandate. A trade at your limit does not prove your order filled. Queue priority, earlier orders, cancellations and routing matter. R5 documents exchange messages; our tiny exercise is a stipulated FIFO scenario, not a full ITCH parser.

Implementation shortfall compares actual cost against a decision benchmark. For a buy, dollars = Σ fill_qty×fill_price + fees − completed_qty×arrival_price, with unfilled opportunity costs specified separately if the mandate requires completion. Dividing by arrival notional and multiplying by 10,000 gives bps. Benchmarks must be frozen before observing fills.

## Worked scenario

Submit a passive buy of 40 shares at 100.00, with 40 shares ahead. A sell trade of 25 leaves 15 ahead, zero own fill. Another 30 consumes the 15 ahead and fills 15 of ours. An acknowledged cancel removes our remaining 25. Buy those 25 aggressively at 100.04. Arrival midpoint was 100.02; fees are $.004 per executed share. VWAP is 100.025, fees $.16, shortfall$.36, approximately .89982 bps. Passive fills alone would look cheaper while concealing the unfinished mandate.

## Lab procedure

1. Run Project 2 and read its event trace. Reproduce it by hand before altering code.
2. Implement a separate event-driven reducer with integer share quantities and an immutable event log.
3. Add a cancel request followed by a fill before acknowledgment; only the remaining quantity is then canceled.
4. Verify original quantity = filled + canceled + remaining after every event. Reject negative or excessive quantities.
5. Read R5's add/execute/cancel/delete/replace messages. Explain why message sequence gaps should stop a supposedly exact replay.

## Assignments

**A1.** Reproduce the queue and shortfall arithmetic. Compute shortfall if the aggressive price is 100.10 instead, holding the other assumptions fixed.

**A2.** Submit a reducer and tests for partial fills, cancel-in-flight, duplicate event IDs and overfills. Begin with the project reference, then extend it; log what its simplified model omitted.

**A3.** List observations required to estimate rather than stipulate passive fill probability. Explain why Nasdaq order attribution is not a direct observation of a portfolio manager's inventory or reward.

Mastery check: you can explain why a passive strategy may show good prices conditional on filling while being poor for the full mandate.

Check your work with the [answer key](../answers/05_execution.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
