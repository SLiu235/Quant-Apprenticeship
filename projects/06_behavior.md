# Project 6 — Test restricted IRL and the limits of behavioral inference

Lessons: 16–18. Integration effort after lessons: 14–22 hours. Workspace connection: BehaviorIRL and QuantKG.

## Research question and input

Under what observed-state, dynamics and reward-family assumptions does IRL predict held-out actions or help replanning? The reference is entirely synthetic: finite-horizon execution with observed remaining quantity and known transition mechanics. It does not infer intentions from Reddit or daily prices.

## Build it step by step

1. Write state, action, feasibility, transition, feature and reward-unit definitions.
2. Verify soft Bellman probabilities, action masks, gradient recursion and reward/temperature scale invariance.
3. Generate separate training/evaluation episodes with declared seeds. Fit the restricted reward with a fixed cost scale and temperature.
4. Compare held-out action likelihood against a training-frequency baseline and behavioral cloning. Report reward error separately.
5. Run three seeds across three fill settings, including a deliberately wrong fitting model. Preserve all outcomes and optimizer failures.
6. Compare stale policy with oracle replanning under changed mechanics, then write an empirical-feasibility memo for each data tier.

## Student deliverables

MDP/data contract, gradient tests, complete experiment matrix, action-loss/reward-error tables, support diagnostics, transfer report and 200-word empirical go/no-go memo. If no actor logs exist, that memo must decline participant-IRL validation rather than manufacture demonstrations from prices.

## Worked project and interpretation

With trueθ=(1,.12,.65,1.4), the reference fit is approximately (1,.11974,.68083,1.61188). Held-out NLL is .76887 versus generating policy.76827. Numerical derivatives agree to around 1e−9, and jointly scaling reward/temperature leaves probabilities equal to floating-point precision. Policy fit is close while the terminal coefficient differs visibly. On the same 481 active held-out decisions, frequency gives NLL≈1.08312, behavioral cloning≈.83516 and training-estimated-dynamics IRL≈.82411. The oracle fit should be compared with its extra dynamics information disclosed.

Reducing passive fill rates makes the stale policy's shifted NLL≈.81677; replanning with the recovered reward and known changed dynamics gives ≈.75923. The sample conclusion is that the implementation behaves sensibly under favorable known mechanics. It is not empirical evidence of investor utility recovery or successful adaptation to unknown market structure.

## Acceptance and answer guidance

Masks, derivatives, distinct episodes and training-only baselines are hard gates. Do not include absorbing inventory-zero states to inflate action accuracy. Report scale normalization, dynamics information and failure of identification where applicable. Keys 16–18 provide proofs, baseline construction and interpretation.

Data upgrade: observed execution logs can support restricted behavioral studies when state, mandate and costs are recorded. Book messages alone enable order-flow studies but do not necessarily reveal actor identity or objectives. Larger GPUs cannot replace those observations.

## Run and inspect the worked example

From the course directory with the [setup interpreter](../guides/SETUP.md):

```bash
python -m reference.run --project 6
```

[Complete reference code](../reference/p06_irl.py) · [Recorded result](../outputs/p06_irl.json) · [Mastery rubric](../assessments/MASTERY.md). A reference run checks the worked core; the student deliverables deliberately extend it and are graded using the lesson keys and the shared rubric.
