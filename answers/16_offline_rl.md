# Lesson 16 answer key — Establish the support for a sequential decision policy

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Ordinary IS=2 and ESS=2. The estimate is not the same object as self-normalized IS in general, though both happen to equal 2 here. More simulated rollouts reduce Monte Carlo error conditional on simulator dynamics; they do not validate those dynamics against the exchange.

## A2

Validate probabilities in[0,1], behavior probability positive for observed actions, finite rewards and declared target support over all relevant state-actions. Observed-row checks alone cannot prove support for unobserved actions. For two consecutive steps each with target/behavior ratio 2, trajectory weight 4; long products amplify concentration. Example weights (4,0,0,0) yield ESS 1. The solution function accepts an explicit support check and refuses unsupported targets.

A correct answer distinguishes true logging propensities from probabilities fitted after the fact; estimated propensities need their own assumptions, training separation and diagnostics. Do not clip weights silently: clipping changes bias/variance and needs a declared sensitivity report.

## A3

Need decisions, actions, timestamps/receipts, state including order/remaining quantity, fills/cancels, rewards and costs, censoring, episode boundaries, policy/version and propensities if randomized, plus venue/market state. A deterministic logger provides no direct support for actions it never takes in the same state. Modeling can extrapolate under explicit assumptions, but a broad unbiased offline-value claim is not available from that dataset alone. Repair by mapping target actions to actual historical coverage before training an agent.
