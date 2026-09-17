# Specialist build briefs

These are optional branches after the relevant core module. They are supplied project specifications, not claims that specialist implementations already exist. Choose by investment problem and documented skill gap. Each submission needs a contract, tiny independently computed fixture, implementation, failure tests, decision memo and limitations. Consult current primary instrument/venue/provider documentation before replacing a stipulated fixture with a real contract.

## 1. Expected returns, Bayesian views and robust allocation

After Module 4, compare rank weighting, shrinkage expected returns and a Black-Litterman view update on the same frozen forecasts. Express views as a matrix and expected-return vector with explicit confidence assumptions. Vary view uncertainty over a declared grid before viewing portfolio outcomes. Then compare a robust uncertainty-set objective with a simple no-trade band. Deliver feasible weights, turnover, costs, sensitivities and a memo on optimizer false precision. Break it with collinear views and an infeasible constraint set. The decision is whether the forecast evidence warrants a precise allocation at all.

## 2. Long/short exposures and financing

After Modules 4–6, build a synthetic ledger with separate long inventory, short inventory, borrow accrual, financing, collateral and cashflows. Compare dollar-neutral, beta-neutral and factor-constrained targets under stipulated exposures. Inject a borrow recall and a rising borrow rate; distinguish simulated feasibility from actual locate availability. Include gross/net exposure, stress liquidity, short squeeze and margin-trigger scenarios. Completion requires reconciled cash and an explicit response to unavailable borrow. Do not infer beta neutrality from zero net dollars.

## 3. Empirical factor and panel research

After Module 3, formulate an economic mechanism before constructing a characteristic. Build a historical membership panel, point-in-time characteristics and a declared rebalancing horizon. Compare cross-sectional regression and rank portfolios with factor exposures. Add clustered/dependent uncertainty appropriate to the sampling design. Break it with a duplicated join, revised fundamentals and a delisted instrument omitted from the panel. The required conclusion separates incremental forecasting, factor compensation and feasible net returns.

## 4. State-space, Bayesian and regime models

After Modules 3 and 5, compare a fixed-parameter baseline, a rolling estimate and a filtered state estimate. Separate filtering from smoothing: a smoother using future observations cannot masquerade as a live state. Test a known synthetic regime transition and a noisy no-transition fixture. Compare predictive loss and calibration, not retrospective regime labels alone. Add complexity only if it improves a frozen evaluation or a useful uncertainty decision. Deliver parameter sensitivity, regime uncertainty and the action that uncertainty changes.

## 5. Multiple testing and backtest overfitting

After Module 3, generate a null research universe and log every tried variant. Compare an unadjusted best-result selection with a predeclared multiple-testing procedure; then implement a Deflated Sharpe Ratio or backtest-overfitting diagnostic directly from its primary paper with explicit dependence and moment assumptions. Validate limiting cases and formula conventions independently. Preserve correlations among candidate strategies when modeling selection. The acceptance criterion is calibrated behavior on null simulations and honest interpretation, not producing a smaller p-value.

## 6. Execution desk: queues, adverse selection and capacity

After Module 6, construct an event tape with visible depth, trade flow, cancel requests/acknowledgments and sequence gaps. Compare aggressive IOC, passive posting, TWAP and a schedule using forecast volume. Keep queue priority stipulated unless observed data can support a richer claim. Calculate conditional fill prices, post-fill markouts, full-mandate shortfall and unfilled opportunity costs. Sweep order size with fixed signal assumptions to investigate capacity. Completion requires order conservation, side-correct TCA and a case where apparently cheap passive execution is worse for the mandate.

## 7. Futures, rolls and options execution

After Modules 5–6, use an explicit synthetic contract specification with multiplier, tick size, expiry and settlement convention. Reconcile price changes to dollar P&L and separate a futures roll from a continuous-series adjustment. For options, price a multi-leg order from stipulated bid/ask quotes and simulate legging risk and incomplete fills; distinguish model value from executable prices. Inject a wrong multiplier, expiry mismatch and stale underlying. Recheck real exchange specifications when adapting. Completion requires a hand-reconciled cash/position ledger and a scenario where trading the quoted theoretical edge is infeasible.

## 8. Auctions and ETF mechanics

After Module 6, build a stipulated single-price auction matching fixture with explicit order priority, imbalance and cutoff rules. Model an ETF basket, cash component and transaction costs; separate secondary-market trading from creation/redemption assumptions and authorized-participant access. Break the model with stale underlying prices and a halted constituent. Investigate whether an apparent discount is executable after basket costs and timing. Deliver an evidence checklist for applying the model to a real venue rather than assuming the toy auction rules are universal.

## 9. Data scale, concurrency and infrastructure

After Module 7, measure the same batch query in a file-based analytical design and a transactional database design. Record row count, memory, wall-clock latency and concurrency assumptions. Add schema evolution and an interrupted ingest fixture. Profile before optimizing; introduce streaming only for a concrete latency need. If a container, queue, REST/gRPC interface, cloud service or Kubernetes deployment is proposed, provide the smallest alternative and an observed requirement it cannot meet. Completion is reliable recovery and adequate measured performance, not the number of tools installed.

## 10. ML lifecycle and advanced AI

After Modules 7–9, train a baseline with explicit feature/model versions; promote through a registry state, run batch inference, and implement rollback on schema mismatch. If online inference is needed, define latency and availability budgets first. Compare a time-series neural model, text embeddings or transformer against the appropriate fixed baseline. For RAG, separately evaluate retrieval, reranking and answer faithfulness; for GraphRAG, identify a relationship query retrieval cannot answer; for an agent, identify a task requiring planning rather than a fixed workflow. Add model routing only with measured quality/cost evidence. Keep tool execution permission separate from retrieved document content.

## 11. RL, inverse RL and causal claims

Use [Lessons 12](../lessons/12_graphs_causality.md), [16](../lessons/16_offline_rl.md), [17](../lessons/17_inverse_rl.md), [18](../lessons/18_transfer.md) and [the behavioral project](../projects/06_behavior.md). Build a restricted synthetic environment with observable states/actions and known reward to test identification before using any observational dataset. Compare behavior cloning, action-frequency and simple decision rules. Challenge off-policy support, reward nonidentifiability and misspecified dynamics. Predicting a price response does not identify a trader's utility. State which additional observations or interventions your inference requires.

## 12. PM decision casebook

After each meaningful empirical project, write a one-page case: market belief; your differentiated belief; evidence; what may already be priced; catalyst; horizon; payoff scenarios; costs; hidden exposures; proposed size; invalidation; reduce/exit rules. Use stipulated numbers first. Calculate expected net payoff and position-level stress loss, then recompute under a plausible error in the central assumption. Decide whether to trade, gather evidence or reject. Completion requires a decision consistent with both the evidence and the portfolio's constraints, including a well-reasoned no-trade result.
