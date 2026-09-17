# Lesson 13 answer key — Evaluate time-series models under regime change

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

For E=2(ŷ−y)/n, ∂L/∂W2=HᵀE and ∂L/∂b2=ΣE. Hidden derivative G=(E W2ᵀ)⊙(1−H²); ∂L/∂W1=XᵀG and ∂L/∂b1=ΣG. Include regularization terms if specified.8×8×1024²×4=268,435,456 bytes=256 MiB. A causal attention mask blocks future token positions, not future information baked into preprocessing or pretrained weights.

## A2

The numerical solution supplies a small NumPy implementation, early-stopping checkpoint copy and gradient check. Standardize with training statistics only; preserve validation for stopping/width selection. Report both widths, stopping epochs, seeds and all scores. A correct negative comparison earns full credit. Finite differences should agree to around 1e−5 or better on a small float 64 fixture, accounting for relative scale. Do not impose a “must beat ridge” pass criterion.

Use future perturbation on fixed candidate training/prediction code; selecting a checkpoint on later validation labels intentionally depends on those labels and must not be confused with a historical pre-validation deployment claim.

## A3

Do not promote from the best seed alone. Choose a specified seed/ensemble procedure using development evidence and estimate its paired uncertainty across market dates on independent data. More GPU allows larger controlled sweeps or faster iteration; it does not create more regimes, fix receipt clocks or establish foundation-model historical availability. Upgrade data when uncertainty is population/market coverage; upgrade compute when a measured runtime bottleneck prevents the specified experiment.

Repair: match all model input dates and selection opportunities before attributing a difference to architecture.
