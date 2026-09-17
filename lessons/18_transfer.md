# Lesson 18 — Challenge learned behavior under misspecification

Prerequisites: Lesson 17. Suggested effort: 6–8 hours, including the lab. Project: 6.

## Recovery under your own simulator is the easiest test

When the generating process and fitted family match, good recovery shows that the optimizer can solve a favorable inverse problem. A professional study also perturbs the assumptions. Dynamics, reward features, actor heterogeneity, observation noise and selection can all change the mapping from actions to utility. A preference coefficient may absorb a misspecified fill model.

Separate three experiments: reward recovery under known correct dynamics; policy prediction with dynamics estimated only from training data; transfer to changed mechanics or held-out actors. Use behavioral cloning as a predictive competitor and simple heuristics as decision baselines. IRL earns its complexity if its structure helps an identified task such as replanning under a validated change, not merely because its parameter names sound economic.

Project 6 reduces passive fill probabilities from(.60,.25) to (.35,.10) for normal/thin conditions. Replanning with recovered rewards and the new known dynamics beats applying the stale policy in this synthetic fixture. This is an oracle transfer demonstration: in a market, the changed dynamics would need measurement or estimation. The oracle is an upper-information comparison, not an implementable production model by default.

## Worked confounding example

An actor rarely uses passive orders. ExplanationA: urgency is high. ExplanationB: passive fill probability is low. If your model fixes passive fills too optimistically, it may infer urgency to explain behavior. More demonstrations under the same unobserved mechanics may tighten a confidence interval around the wrong parameter. Interventions that change fills while preserving the actor objective, or observed fill outcomes, can help distinguish explanations under additional assumptions.

Use sensitivity surfaces, not only point estimates. Refit over plausible dynamics and normalization settings; report policy distance, likelihood and utility variation. Out-of-family adversaries include hidden private signals, a non-Markov policy, regime switches and inconsistent actors. A fail condition should be defined before looking at which perturbation preserves the story.

## Lab procedure

1. Run the shift comparison and label each input as observed, estimated or oracle.
2. Generate three simulator seeds, holding the experimental design fixed. Keep within-seed training/evaluation episodes distinct.
3. Refit using intentionally wrong fill dynamics and compare parameter changes with held-out action loss.
4. Add an actor whose actions depend on a hidden variable. Test whether residual errors concentrate in omitted-state regimes.
5. Read R17 on generalizability. Distinguish reward equivalence from ordinary finite-sample noise.

## Assignments

**A1.** Interpret the stale versus replanned losses and explain the oracle advantage. State a scenario in which reward error is large but policy error is small.

**A2.** Submit a sensitivity matrix for three seeds and at least three fill settings, including one misspecified fit. Report all fits, support and optimizer failures. Do not select the best recovered coefficient after inspection.

**A3.** Design a data/compute ladder for the original graph-IRL idea: public bars/text, event-level book data, and consented/internal execution logs. State the strongest verifiable claim at each tier.

Mastery check: you can recommend abandoning participant IRL at one data tier while retaining a useful public-response research question.

Check your work with the [answer key](../answers/18_transfer.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
