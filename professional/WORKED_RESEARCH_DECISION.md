# Worked research decision — actual local model comparison

This is an example produced by the package author, not submitted learner work. Results below come from [the saved model lab](../outputs/model_lab/model_lab_report.json). Data are real local snapshots for a retrospectively selected four-issuer universe. The evaluation dates are already inspected development material.

## Question and procedure

Does a small nonlinear predictor improve squared-error forecasting over simple price-feature alternatives? Five procedures were declared: zero return, ridge, ridge with lag-1 input removed, and MLPs of widths 4 and 8. Features and target scaling use training data; MLP checkpoints use only validation data within a fixed 200-epoch budget. The selected procedure is locked in the experiment book before final-block results are recorded. No post-selection refit is performed in this lab.

## Observation

The width-8 MLP was selected on validation. On the 75-date, 300-observation evaluation block, its MSE was approximately 0.00174171, compared with 0.00170795 for the zero-return baseline. Candidate-minus-zero average loss was +0.00003376. The specified five-date moving-block descriptive interval was approximately [−0.00005359, +0.00014750]. It includes zero. These are loss units, not portfolio returns or probabilities of profitability.

Ridge and the width-4 MLP also did not beat zero by point-estimate MSE on this block. Reporting the best evaluation model as if it had been selected beforehand would change the experiment after seeing the answer.

## Decision

Do not prefer this selected MLP on the basis of demonstrated incremental forecasting value. This result does not establish that deep learning is unsuitable for markets. It establishes that this small model, these features, this selected sample and this particular protocol do not provide the claimed improvement. The limited sample and conditional interval also do not prove equivalence among methods.

Before another model sweep, inspect whether the question and observations can support a useful prediction: missing information, economic horizon, target noise, coverage and baseline strength. A new representation or dataset needs a mechanism-based justification and a new declared experiment. Another random seed alone is not a cure for inadequate evidence.

## What remains unresolved

The original vendor snapshots do not establish historical receipt times or historical universe membership. There is no prospective sample, no capacity estimate and no execution test for these models. The experiment book records this workflow but cannot undo prior exposure to the data. Its date-block interval is not adjusted for arbitrary unlogged model search. The next decision is whether a particular data or representation improvement is worth investigating, not whether to trade the reported forecast.
