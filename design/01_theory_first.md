# Design round 1 — a theory-first graduate course

**Editorial simulation.** The CEO voice below is an invented research-review role, not the opinion of a real executive or firm.

## Proposed design

Start with six theory blocks: asset pricing, stochastic processes, supervised learning, reinforcement learning, market microstructure and portfolio optimization. Assign textbook problem sets, then ask the student to build a trading agent as a final project. Dedicate most compute to a deep time-series model and an IRL estimator. Evaluate the final project with predictive accuracy and a backtest Sharpe ratio.

This design has a coherent mathematical dependency chain. A student could derive a Bellman equation and explain regularization. It provides too little practice determining whether a dataset can answer the question.

## Simulated CEO critique

“You are hiring someone to decide what evidence the desk needs, not just to solve a supplied optimization problem. The student can score highly while using revised data, hindsight-selected stocks and imagined fills. A final Sharpe number conceals the research search. Your reinforcement learner may have learned an artifact of your simulator. Where is the baseline? Who can reproduce the decision? What would make you stop spending money?”

Specific objections:

1. A theory sequence postpones the first empirical failure until the end.
2. Forecasts, positions, execution actions and motives are treated as interchangeable targets.
3. Statistical accuracy is not enough to size a position or pay for inference.
4. Changing market sessions are appended as a topic instead of changing the data contract and operating model.
5. A final project cannot repair six months of inadequate experiment discipline.

## Revision decision

Retain necessary derivations, but introduce them at the moment a project needs them. Start with an independent audit of an existing negative result. Require decision-time availability, simple baselines and an economic interpretation in every research memo. Move IRL after supervised evaluation and execution accounting. Carry an experiment ledger across the whole course.

Rejected request: make the first project a live trading contest. Live PnL confounds skill, sample noise, risk and market exposure; it is unnecessary for learning the research process.

Next design: an eight-project apprenticeship with explicit artifacts and review gates.
