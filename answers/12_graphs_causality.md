# Lesson 12 answer key — Distinguish a discussion graph from knowledge propagation

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

The release is a shared cause of posts and trades. A possible estimand is the average difference in a prespecified action probability under randomized delivery versus nondelivery of a particular message at time t, for an eligible participant population and horizon. Define whether others' exposure is held fixed or allowed to respond: network interference changes the estimand. Randomization, compliance, measurement and spillover assumptions would still need evidence. “Influence of knowledge” without an intervention is underspecified.

## A2

Use typed edges `(source,target,type,event_at,available_at,coverage_state)`. Filter before aggregation and distinguish count 0 under observed coverage from unknown coverage. A future-edge perturbation must leave past counts unchanged. For learned embeddings, training data and node attributes must satisfy the same cutoff; filtering only the adjacency query is insufficient. A valid small implementation may use count features and avoid fitted embeddings entirely.

## A3

The archive lacks actual exposure, participant execution decisions, remaining mandates and full inventory. It also has engagement-conditioned comment collection and missing receipt/edit history. Therefore it cannot validate participant reward recovery or causal propagation. A defensible study is an explicitly selected-sample forecast comparison of observable discussion features, with no causal or actor interpretation and an acknowledgement that collection bias limits even broader predictive generalization. Acquiring complete prospectively sampled discussion can improve coverage; it still does not create observed investor state.

Repair: replace every use of “influence” with the exact field you measured. If the claim becomes unsupported or incoherent, narrow it before modeling.
