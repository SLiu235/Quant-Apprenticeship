# Lesson 9 — Design walk-forward evaluation and a research ledger

Prerequisites: Lessons 7–8. Suggested effort: 5–7 hours, including the lab. Project: 3.

## Time order is necessary, not sufficient

Use training data to fit parameters, validation data to select a declared candidate set, and untouched data for the final selected procedure. In rolling evaluation, refitting on labels that have genuinely arrived is allowed if the schedule is prespecified. Refitting after every bad day because it looked bad is a change to the procedure.

Labels can overlap. A five-day return starting Friday may include prices in next week's validation interval. Purge training observations whose label-information intervals overlap evaluation information in a way prohibited by your protocol. An embargo can address boundary contamination, but an arbitrary one-day gap does not cure a five-day overlap. Compute exclusion from the actual interval definitions and receipt clocks.

Model search creates selection bias even when each candidate backtest is chronologically correct. Under 100 independent null tests at 5%, the probability of at least one false rejection is 1−.95^100≈.994. Financial tests are correlated, so that exact formula is illustrative; the basic search problem remains. Record features, hyperparameters, preprocessing, universes and abandoned models, not just neural-network checkpoints.

## Worked evaluation design

Project 3 fixes a three-value ridge grid, chooses on the middle 20% of ordered dates, and refits every 20 later dates using completed prior labels. Its final 20% evaluates a procedure that learns from prior evaluation-period labels on a declared schedule. This is a prequential design, not a single permanently frozen model. In the course, the result is already visible and remains teaching evidence, not fresh confirmation.

A useful uncertainty report distinguishes variation over test dates, over training seeds, over market regimes and over research choices. More seeds reduce uncertainty about optimization; they do not create more independent market history.

## Lab procedure

1. Draw the training, validation and evaluation intervals in a plain table.
2. Create label intervals for five overlapping five-day targets; mechanically mark forbidden overlaps.
3. Write an experiment ledger entry before modifying the baseline. Include one primary metric and a budget of candidate variants.
4. Reproduce the reference's refit log. Check that no refit includes that day's target.
5. Read R4's multiple-testing argument and R1's resampling chapter. Identify which randomness your interval covers.

## Assignments

**A1.** Calculate the 100-test example. For a label spanning days 8–12 with evaluation starting day 10, explain whether a training feature timestamp at day 8 is enough to admit it.

**A2.** Implement interval-based purge logic with boundary tests. Write a nested chronological selection protocol for comparing ridge and one nonlinear model without repeatedly selecting on the final block.

**A3.** Write a research ledger containing the original baseline, a sign-reversal idea and a text-feature idea. Declare their status after viewing the existing results, a stopping rule and a genuine independent confirmation plan.

Mastery check: you can state exactly which procedure was selected, when it was selected and what evidence remained unavailable to that selection.

Check your work with the [answer key](../answers/09_validation.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
