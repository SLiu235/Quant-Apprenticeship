# Lesson 1 — Define what the experiment can establish

Prerequisites: graduate statistics and Python. Suggested effort: 3–4 hours, including the lab. Project: 1.

## Learn the distinction

A quant researcher turns a proposed mechanism into a measurable question. Consider four progressively stronger claims: text predicts a price response; observations predict another trader's action; actions identify that trader's utility; using the prediction improves a feasible decision. Each requires extra observations and assumptions. A sophisticated estimator cannot create an unobserved target.

Our case is a real recent Reddit/price pilot, not a participant-IRL test. It contains 493 eligible issuer-days for ASML, MU, SNDK and WDC. Its saved test contains 139 issuer-days on 52 dates from December 11, 2025 through February 27, 2026. These outcomes have already been inspected. They are development material for this course, even if a file calls them “test.” Read the [pilot report](../../BehaviorIRL/results/reddit_recent_2026/RECENT_DATA_REPORT.md).

Let I_t be information usable at 09:25 New York time. The target is r = 10,000(Close/Open − 1), in basis points, categorized negative below −25, neutral on [−25,25], positive above 25. The model estimates P(Y | I_t, archive inclusion). That last condition excludes many issuer-days. It cannot silently become a claim about all Nasdaq stocks.

The estimand is an expected loss difference for a stated population and weighting. Choose it before the architecture: “On eligible issuer-days, does a frozen text feature reduce date-weighted negative log likelihood relative to a price-only feature?” Lower loss is useful evidence about probabilities. It does not measure dollars.

## Worked example

A binary forecast gives 60% probability to +1 bp and 40% to −5 bps. The most probable direction is up, but E[r] = .6(1)+.4(−5) = −1.4 bps. Even perfect classification calibration would not make a long position attractive in this example. A trading rule needs payoff magnitudes, fees and execution information.

A contract therefore records observation, population, information cutoff, target, comparison, weighting, success rule, exclusions and decision. Success must be falsifiable. “The model learns market psychology” is not a testable contract; “its prespecified paired loss difference is negative on an independent sample” is.

## Lab procedure

1. Open the pilot report and `BehaviorIRL/real_data/reddit_recent_protocol/protocol.json` without changing them.
2. Copy the [research contract template](../templates/research_contract.md) into your submission directory.
3. Fill its fields from the actual protocol. Keep observed facts separate from assumptions.
4. Write what would change your mind. Separate a negative forecast result from a failure to observe participant behavior.
5. Read R1, “Statistical Learning,” in the [reading library](../guides/READINGS.md), focusing on prediction versus inference.

## Assignments

**A1.** Write a contract in at most 180 words with all nine fields above. State whether its target is an investor action.

**A2.** Recalculate the binary example. Add a 2 bp round-trip cost. Identify two additional objects needed to turn the pilot's three-class probabilities into expected net returns.

**A3.** Write a 150-word decision explaining why a positive result on this sample would not identify motives or prove general Nasdaq alpha. Connect the prediction/inference distinction in R1 to one concrete missing variable.

Mastery check: you can describe the target without mentioning IRL, and distinguish “not supported by these data” from “impossible in principle.”

Check your work with the [answer key](../answers/01_research_contract.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
