# Lesson 21 — Operate a paper research system and recover from failures

Prerequisites: Lessons 5, 19–20. Suggested effort: 6–8 hours, including the lab. Project: 7.

## A model is only one component of a decision service

A paper system needs data freshness checks, valid-session rules, model/schema compatibility, exposure limits, an order state machine, durable events and reconciliation. Separate prediction from authorization to act. A forecast can be produced while the decision service refuses a new order because its quote is stale or state is unreconciled.

Halting new orders does not erase outstanding orders or fills. The system must keep receiving and reconciling authoritative execution reports. Dropping fills during a halt creates an incorrect inventory exactly when the desk needs accuracy. A resume requires fresh data, reconciled cash/positions/open orders and an explicit operator policy. The course reference has no broker connection and intentionally omits a production journal, short handling and full cash-risk controls.

Monitor input distribution, missingness, event-time/receipt lag, prediction distribution, delayed-label performance and economic outcomes separately. A drift alarm can reflect market change, a vendor outage or a schema bug. Do not automatically retrain on an unexplained data defect. Define alert thresholds and an investigation procedure; repeated monitoring also creates a multiple-testing problem.

## Worked event trace

A paper account begins with $10,000. A40-share order receives 15 at 100.00, then a duplicate of that fill. The duplicate must have no financial effect. A stale quote halts new submissions. A subsequent 25-share fill at 100.04 still applies, leaving 40 shares and $5,999 cash. Resume before reconciliation fails. Matching the authoritative balances/open orders permits a supervised resume. At 100.02 midpoint, equity is $9,999.80 before fees; this trace isolates fill accounting from the fees in Project 2.

## Lab procedure

1. Replay Project 7 and reconcile every state transition by hand.
2. Inject stale data, duplicate fill, invalid overfill and broker-state mismatch separately. Preserve pre-error state for invalid mutations.
3. Write an incident runbook: detect, contain new risk, reconcile, diagnose, repair, replay and approve resume.
4. Add a durable append-only journal in your student extension; simulate process restart from a checkpoint plus subsequent events.
5. Review R5's sequence-dependent feed semantics and R11's tool-authority principles. Market data and generated text are inputs, not authority to bypass controls.

## Assignments

**A1.** Calculate cash, shares and equity in the worked trace. Explain why “halt means ignore all events” is wrong.

**A2.** Submit fault-injection tests and a restart/replay journal extension. Verify duplicate events across restarts, overfills and mismatched reconciliation cannot silently alter accepted state.

**A3.** A social-text feature becomes mostly missing overnight. Write an incident decision distinguishing source outage, real activity change and model drift. Specify what evidence is required before retraining or resuming.

Mastery check: the system can explain why it declined a decision and reconstruct every accepted fill after interruption.

Check your work with the [answer key](../answers/21_operations.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
