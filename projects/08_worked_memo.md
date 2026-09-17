# Worked capstone memo — do not promote the frozen public-text feature

## Decision

Retain the recent public-signal experiment as a negative exploratory result. Do not promote this model on the evidence available. Consider a prospectively logged social/price panel only if its acquisition cost is justified by a clearly bounded next question.

## Question and population

The experiment asks whether a fixed lexical post feature improves a 09:25 ET forecast of same-day open-to-close return categories over a market-feature baseline. It covers selected eligible issuer-days for ASML, MU, SNDK and WDC, not the Nasdaq population. The saved evaluation contains 139 issuer-days on 52 dates, December 11, 2025–February 27, 2026. The archive supplies public text and vendor price bars, not investor orders or mandates.

The primary estimand is the mean, across equally weighted dates, of within-date paired public-minus-market negative log likelihood. Negative would favor public text. The historical protocol and saved fitted predictions are retained in BehaviorIRL. This course memo is an independent retrospective audit; the evaluation outcomes are already known.

## Evidence

Independent recomputation gives market NLL .9605763 and public .9773731. Their row-weighted difference is +.0167968. The equal-date difference is +.0146499 with an exploratory three-date moving-block 95% interval[.0064225,.0245799], using 1,000 replicates and seed 42. Block lengths 1,5 and 10 remain unfavorable in the recorded sensitivity, but they do not remove dependence or selection uncertainty. The unconditional frequency baseline's NLL .9456656 is better than either model.

The graph model's NLL .9867375 is worse still, but its central limitation is measurement: comments were collected according to eventual engagement, and same-thread participation is not observed reading, endorsement or causal propagation. No actor-IRL estimator was evaluated on these data.

## What limits the conclusion

Post creation plus 60 seconds is assumed historical availability; actual receipts and edit history are missing. Missing social days and the four-name selection restrict the population. Engagement-conditioned collection cannot be repaired by timestamp filtering alone. These issues do not justify ignoring the negative result; they prevent a stronger general claim either for or against social information.

A probability-loss difference is not trading PnL. This pilot has no verified fills, payoff-within-class model, impact/capacity study or complete financing assumptions. Daily ordinary-session bars do not validate overnight execution or a future exchange schedule. Locally newer price bars do not extend the social archive's coverage.

## Next experiment and stop rule

Before another model search, assess whether a predetermined issuer/source universe can be logged prospectively with actual receipts, versions, outages and a sampling rule independent of eventual engagement. Freeze the downstream baseline, representation, candidate budget, retraining schedule and evaluation before examining new outcomes. Use the current archive only for development and acquisition tests.

Stop the acquisition effort if license, receipt history or coverage cannot support the stated question at reasonable cost. If acquisition succeeds, test one representation change against the baseline on fresh paired observations. A favorable result would justify the next evidence stage, not immediately establish participant motives or tradable alpha.

## Reproduction and committee challenges

Run `python -m reference.run --project 8` from the course directory. Inputs and metrics are linked by Project 1's prediction hash. Challenges resolved: class order and paired populations checked; date weighting independently reproduced; all declared block sensitivities retained. Remaining limitations: selected collection, assumed availability and absent execution/actor evidence. These are data limitations, not defects claimed to be fixed by the course code.
