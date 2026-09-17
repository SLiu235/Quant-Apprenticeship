# Lesson 17 — Fit a restricted utility model and test identification

Prerequisites: Lesson 16 and differentiation. Suggested effort: 7–9 hours, including the lab. Project: 6.

## IRL is an inverse problem with equivalences

Forward planning maps a reward and dynamics to a policy. IRL tries to infer a reward model from actions. Multiple rewards can generate the same policy, and uncertainty about dynamics can be mistaken for preferences. Begin with a restricted family r_θ(s,a)=φ(s,a)ᵀθ and explicitly observed state/action trajectories. Do not substitute price changes for investor actions.

For finite-horizon maximum causal entropy planning, use Q_t(s,a)=r_θ,t(s,a)+Σ_s'P(s'|s,a)V_{t+1}(s'), V_t(s)=τ logΣ_a exp(Q_t(s,a)/τ), and logπ_t(a|s)=(Q_t−V_t)/τ. Feasibility masks remove impossible actions. Stable log-sum-exp avoids overflow. Causal entropy accounts for sequential decisions rather than treating complete paths as arbitrary independent class labels (R16).

The demonstration objective is negative mean logπ of observed actions, optionally with regularization. Differentiate backward: dQ=φ+P dV_next; dV=Σ_aπ dQ; dlogπ=(dQ−dV)/τ. Validate derivatives numerically before interpreting recovered coefficients.

Reward scale is not identified if temperature is also free. Multiplying all rewards and τ by positive c scales Q,V by c and leaves π unchanged. Other equivalences, including potential-based shaping under appropriate boundary conditions, can preserve behavior. Fixing one cost coefficient and temperature removes one ambiguity, not all possible reward nonidentifiability (R17).

## Worked reference

Project 6 uses 48 synthetic states and three actions: wait, passive, aggressive. Remaining quantity is observed by construction. The true normalized coefficients are (1,.12,.65,1.4); 180 training episodes and 80 held-out episodes come from known dynamics. The estimated vector is approximately (1,.11974,.68083,1.61188). Near-matching action likelihood does not imply exact coefficient recovery. Terminal-shortfall preference is less precisely recovered in this finite sample.

## Lab procedure

1. Inspect `BehaviorIRL/behavior_irl/mdp.py` to map every feature to its units and sign.
2. Run Project 6 and reproduce the probability invariance under jointly scaling θ and τ by 3.
3. Compare analytic dlogπ with central differences on feasible actions only; impossible actions have −∞ log probability.
4. Fit on training episodes and compare held-out action loss to the generating policy and a simple action-frequency/behavioral-cloning baseline.
5. Read R16 and R17. Write what the normalization does and does not identify.

## Assignments

**A1.** Derive the soft-policy gradient recursion and prove the joint scale invariance by backward induction.

**A2.** Reproduce the synthetic fit and gradient check. Add a simple frequency baseline trained on active decisions, masking impossible actions. Report held-out likelihood and parameter error separately.

**A3.** Write the observational requirements for applying this model to another participant. Explain why the recent public-price experiment cannot provide them and why known-simulator recovery is only one validation layer.

Mastery check: you report restricted-model utility, policy fit and transfer separately; “recovered psychology” is not an acceptable conclusion.

Check your work with the [answer key](../answers/17_inverse_rl.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
