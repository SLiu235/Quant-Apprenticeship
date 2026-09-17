# Lesson 16 — Establish the support for a sequential decision policy

Prerequisites: Lessons 5, 9 and 15. Suggested effort: 6–8 hours, including the lab. Project: 6.

## Prediction is not policy evaluation

An MDP specifies state s, action a, transition P(s'|s,a), reward r and horizon/discount. A policy changes the distribution of future states; evaluating a predictor on fixed labels does not evaluate that intervention. State must contain the information needed for the Markov approximation. Remaining quantity and time-to-deadline are essential in an execution task; omitting them can make identical-looking book states require different decisions.

Offline RL learns from logged behavior. If the logging policy rarely took an action in a state, the dataset gives little evidence about its consequence there. A simulator or function approximator can produce a number anyway. The number's existence is not evidence of support. R15 discusses these coverage and extrapolation issues; conservative methods reduce some overestimation but do not manufacture missing counterfactuals.

For a contextual one-step case, inverse propensity weighting estimates target-policy value using mean[π(a_i|s_i)/b(a_i|s_i) × reward_i], assuming known logging propensities, overlap and appropriate consistency/exchangeability. Sequential trajectory ratios multiply these factors and can have enormous variance. Effective sample size (Σw)²/Σw² reveals concentration but does not cure confounding or wrong propensities. Doubly robust estimators combine outcome and propensity models under assumptions; neither model can be judged solely by in-sample fit.

## Worked example

Logged behavior chooses actionA with probability .5 and B with .5. A target always choosesA. Four logged rewards/actions are (A,1),(B,0),(A,3),(B,2). Weights are 2,0,2,0; ordinary importance sampling gives (2+0+6+0)/4=2. ESS=16/8=2. If behavior never choseA, the target's value would be unsupported, not zero.

## Lab procedure

1. Define an execution MDP with remaining quantity, spread state, signal and time index; specify which are observed versus simulated.
2. Implement the one-step importance estimate and support diagnostics on the worked fixture.
3. Compare a simple policy with a candidate in a held-out simulator using identical initial conditions/seeds, while reporting that mechanics are synthetic.
4. Create an unsupported-action fixture and make the evaluator refuse a value claim.
5. Read R15 on offline dataset characteristics and extrapolation. Identify how a logged market dataset differs from a game benchmark.

## Assignments

**A1.** Reproduce the estimate and ESS. Explain why increasing simulator rollouts cannot remove uncertainty about real unobserved transition dynamics.

**A2.** Implement one-step importance sampling with propensity validation and a support-failure result. Add a two-step ratio example and report how weight concentration changes.

**A3.** Specify the minimum execution log needed for offline policy evaluation, including logging probabilities or their limitations. Explain how a deterministic historical strategy restricts evaluation.

Mastery check: the evaluator reports “not identified/supported” when appropriate rather than turning absence of evidence into an estimated zero reward.

Check your work with the [answer key](../answers/16_offline_rl.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
