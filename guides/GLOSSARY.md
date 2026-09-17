# Working vocabulary and units

| Term | Meaning in this course | Common confusion |
|---|---|---|
| Estimand | Precisely defined quantity for a population and weighting | A model name or vague research aim |
| Observation | Unit recorded/scored, such as issuer-day | An independent trial |
| Availability | Earliest usable time including receipts, versions and computation | Creation timestamp alone |
| Point-in-time | Uses only information and identities knowable at the decision | A current database queried for old dates |
| Return | Price/cashflow change divided by an explicit capital base | Dollar PnL |
| Basis point | .0001 in decimal return, or .01 percentage point | One percent |
| NLL | Negative natural log probability of the realized class | Expected return or dollars |
| Brier score | Sum of squared class-probability errors, then observation mean | This course does not divide the class sum by class count |
| Calibration | Agreement between forecast distributions and realized frequencies/moments | Accuracy alone |
| Turnover | Traded absolute notional divided by capital under a stated convention | Always equal to weight changes between end-of-day portfolios |
| Implementation shortfall | Actual implementation cost relative to a frozen decision benchmark | Conditional fill price alone |
| Capacity | Position/order scale compatible with liquidity, cost and risk limits | Exchange-reported daily volume |
| Covariance | Joint variation in compatible horizon/units | A correlation matrix without volatility scales |
| Second moment | E[r²]; equals variance plus squared mean | Always centered variance |
| QLIKE | Here log(v)+r²/v for positive second-moment forecast v | A mean-return score |
| Drift | Change in inputs, labels, relationships or operation | An automatic instruction to retrain |
| Behavior cloning | Supervised action prediction from state | Reward identification |
| Offline RL | Policy learning from logged actions/outcomes | Counterfactual outcomes observed for all actions |
| Support/overlap | Relevant target actions have evidence under the logger | A network can output a Q value |
| IRL | Inference of a restricted reward model from observed behavior | Recovering a person's true motives uniquely |
| Temperature | Stochastic-choice scale in the soft policy | A freely comparable utility coefficient across normalizations |
| Oracle input | Information supplied for a favorable controlled comparison | Data available to an empirical learner |
| Discussion edge | An observed relation such as reply or same-thread participation | Reading, endorsement or causal influence |
| Retrieval | Selecting eligible evidence documents | Guarantee that generated claims are entailed |
| Model-date leakage | Later knowledge may be embedded in model parameters | Fixed by changing the date in a prompt |
| Prequential evaluation | Evaluate a prespecified procedure that updates on genuinely arrived prior labels | Arbitrary post-result retraining |
| Reproduction | Recover a stated computation from its artifacts | Proof that its research design was valid |
| Fresh evaluation | Outcomes unavailable to model/procedure selection | An inspected dataset in a newly named folder |

When reading a new paper, translate its notation into this table: population, clock, target, decision, score, economics and assumptions. The same word can have different conventions; state yours before comparing numbers.
