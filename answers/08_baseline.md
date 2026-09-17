# Lesson 8 answer key — Make a simple model earn its complexity

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Differentiate (1/n)||y−Zw||²+λwᵀDw: gradient 2Zᵀ(Zw−y)/n+2λDw=0, giving the stated system. The intercept has D_00=0. Cost 8−.8×5=4 bps; flat-to-flat unit gross costs 2×5=10 bps. A coefficient on a feature scaled by 100 is divided by 100 for the same prediction, changing its squared penalty by 10,000 unless scaling/penalty are adjusted.

## A2

Use the actual Project 3 refit dates and `last_label_date < decision_date`. Fitting one scaler on the entire dataset fails. For a future-perturbation test, hold the model-selection protocol fixed and change a return strictly after the decision under test; its features, scaler and fitted weights must not change. If you test an earlier validation prediction after selecting λ on later validation outcomes, selection itself creates a dependency: compare raw candidate predictions or freeze λ first. This distinction prevents a misleading test.

## A3

Recorded model MSE≈.001743422 versus zero≈.001707953: the ridge is worse. Gross mean≈−3.93535 bps/day; with 5 bps one-way cost,≈−13.93535 bps/day. Negative break-even cost ≈−1.96767 bps means this sample would require a subsidy, not merely cheap execution. Positions are a naive sign mapping with assumed open/close marks; no tradable-performance claim follows.

Negating the strategy uses observed results to choose a new rule. Register it as another development experiment and evaluate later independent data. Exposure diagnostics can include market beta estimated on training data, gross/net weights and sector concentration; with four related names, sector generalization is especially limited. Repair by distinguishing a forecast score from a portfolio benchmark return.
