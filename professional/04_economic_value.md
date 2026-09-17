# Research studio — Portfolio value, capacity and execution

[Professional track](../PROFESSIONAL_TRACK.md) · [Evidence rubric](../assessments/PROFESSIONAL_EVIDENCE.md)

## Objective and prerequisites

Determine whether a forecast deserves capital after costs, exposures, signal decay, liquidity and exit requirements.

Enter from Modules 4–6. This is self-paced project work. You are not being assessed by reading it.

## Core knowledge

Evaluate the complete decision chain. Forecast loss estimates predictive quality. A portfolio policy maps forecasts into risk. Execution determines which inventory is acquired and at what cost. Realized P&L then includes exposures that may not correspond to the forecast target.

For this reference, P&L = prior inventory × (arrival midpoint − prior mark) + filled inventory × (close − arrival midpoint) − execution costs. This separates overnight movement from intraday movement and costs. It is an accounting decomposition, not proof that intraday profits are alpha. The new cash/equal-weight/signal grid uses shared calendars, limits and cost assumptions; differing realized exposures still require risk-aware comparisons.

At larger capital, participation constraints may reduce the executed fraction and change the portfolio. Spread, impact, financing, adverse selection and exit liquidity can erode a forecast differently. A simulator with stipulated impact can reveal sensitivity; only supported market observations can calibrate capacity. Consider the marginal contribution to an existing portfolio, including correlation and shared liquidity demands, rather than standalone Sharpe alone.

## Mental model

Allocate to robust marginal opportunity. The relevant alternative may be holding cash, retaining the current portfolio or using a simpler strategy, not merely a different ML model.

## Worked case

With a forecast edge of 8 bps over one hour, waiting 45 minutes may erase the information advantage. A passive order with low costs conditional on filling can still lose at the full-mandate level. Compare the original desired quantity and horizon, including non-fills and adverse post-fill moves.

## Implementation project

Run the 18-scenario synthetic grid. Add an independently calculated horizon decomposition. Align the holding policy to the forecast or model overnight exposure explicitly. Then create a terminal liquidation schedule with partial fills and costs; report unresolved inventory. Add a signal-decay versus urgency experiment and a marginal portfolio-contribution case.

Save independent work under `submissions/professional/04_economic_value/`. Before coding, define requirements, data contracts, assumptions, alternatives and failure detection. Use the [research agenda](../templates/professional/research_agenda.md), [experiment protocol](../templates/professional/experiment_protocol.md), [edge/data card](../templates/professional/edge_data_card.md) and [committee memo](../templates/professional/committee_memo.md) where relevant.

## Failure cases

Standalone prediction gain interpreted as incremental portfolio value; comparing gross and net baselines; hiding terminal inventory; calling a dollar-neutral book factor-neutral; presenting a toy participation cap as measured capacity.

## Debugging exercise

A profitable total replay has negative intraday P&L. Separate overnight, intraday and costs and trace which positions generated each. Change the terminal mark and explain what is realized versus unrealized.

Preserve symptom, competing hypotheses, discriminating evidence, earliest violated invariant, root cause, fix and regression test. Ask for progressively stronger hints if stuck.

## Decision exercise

At ten times capital, only a small fraction of target orders fills and exposure concentrates in liquid names. Choose a lower mandate size, slower horizon, different universe or no trade. Name the evidence needed to distinguish them.

Write your decision before consulting the reference or requesting the mentor's tradeoff analysis.

## Completion evidence

Matched economic comparisons; horizon and exposure attribution; capacity and cost sensitivity; signal-decay case; explicit liquidation/unfilled handling; position-size and exit decisions supported by the available evidence.

Attach evidence for each claim. Missing evidence remains unverified rather than filled with a confident narrative. A meaningful negative result can meet the research objective. Source-code execution alone cannot.

## Optional self-assessment

A signal portfolio earns $100,000, but $140,000 is overnight inventory movement and costs are $20,000. What is its intraday market P&L, and can total profit validate an intraday forecast?

<details>
<summary>Open a hint or answer only when you choose</summary>

Intraday market P&L is −$20,000: 140,000 − 20,000 − 20,000 = 100,000. Total profit does not by itself validate an intraday forecast.

</details>

For mentor review, submit the original attempt, relevant code/data manifest, failure investigation and decision memo. Review will identify what is correct, questionable and wrong, then assumptions and next investigations; it will not automatically replace your work or promote your level.
