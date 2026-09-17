# Lesson 5 answer key — Replay a decision and account for fills

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Trace: after first trade ahead 15/ownremaining 40/ownfilled 0; after second ahead 0/remaining 25/filled 15; after cancel remaining 0/canceled 25. Totalnotional=1,500+2,501=4,001; benchmark=4,000.80; plus $.16 fees gives $.36 shortfall. Bps=.36/4,000.8×10,000=.899820036. At 100.10, notional 4,002.50, shortfall$1.86 and 4.649070186 bps.

## A2

Maintain requested quantity, acknowledged live quantity, filled quantity, canceled quantity and a set of processed event IDs. Cancel-request sets a pending flag; it does not zero remaining. Example: order 40 → fill 15 → cancel request → fill 5 → cancel acknowledgment 20. Final filled 20+canceled 20=40. Duplicate fill event must leave all balances unchanged. A fill of 21 after only 20 remain must raise or halt without applying it. Test order state and cash, not just an emitted status string. A full implementation must reconcile authoritative execution reports even during a halt.

The small P2 reference demonstrates only an acknowledged cancel and deterministic FIFO. It does not implement your complete extension. Project 7 supplies an additional example of duplicate handling and reconciliation.

## A3

Need timestamped submitted order state, acknowledgments, exchange sequence, queue position or a stated estimator, trades/cancels, latency, market state, censored unfilled orders and venue/routing context. Compare predicted fill probabilities against all eligible orders, including those that did not fill. Displayed order IDs and optional member attribution are not investor identities, remaining mandates or full cross-venue positions.

Repair: include an order that never fills. If it disappears from evaluation, your metric is conditioned on success.
