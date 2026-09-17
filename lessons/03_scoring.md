# Lesson 3 — Score forecasts and quantify dependent evidence

Prerequisites: Lessons 1–2. Suggested effort: 5–6 hours, including the lab. Project: 1.

## Proper scores and paired questions

For outcome y and class probabilities p, negative log likelihood is −log p_y. Multiclass Brier score is Σ_k(p_k−1[y=k])², using the sum across classes rather than its average. Both reward honest probabilities in expectation. Accuracy discards most of a probability vector and can conceal costly overconfidence. Natural logarithms give NLL in nats, not basis points.

## Worked score and weighting examples

For p=(.2,.3,.5) and positive outcome, NLL=0.693147 and Brier=.04+.09+.25=.38. For a public-versus-market comparison use the same episodes and targets, then compute δ_i = loss_public,i−loss_market,i. Negative favors public. A missing-model row is not permission to compare different populations silently.

Cross-sectional observations share market shocks. Average paired differences within each date, then average dates equally if that is the contract. For date 1 with one δ=.10 and date 2 with three δ=−.02, the row mean is .01 but the equal-date mean is .04. Weighting changes the question.

A moving-block bootstrap resamples contiguous date blocks, preserving some local dependence. It does not guarantee independence between blocks, fix selection bias, or account for an unrecorded model search. With only 52 dates, report sensitivity and avoid interpreting the interval as a universal long-run guarantee.

## Lab procedure

1. Read `predictions.csv` with the class order negative, neutral, positive. Verify one row per episode/model and matched targets.
2. Write scores independently before opening [reference code](../reference/p01_audit.py).
3. Form paired differences, sort dates, average within dates and compare row/date means.
4. Bootstrap 1,000 replicates, seed 42: choose starts uniformly from 0 to D−b, concatenate b-date blocks and truncate to D dates. Report b=3 primary and 1,5,10 sensitivity.
5. Run `python -m reference.run --project 1` from the course directory using the setup guide's interpreter. Compare [recorded results](../outputs/p01_audit.json).
6. Read R1's resampling discussion. Identify the assumption that ordinary independent-row resampling would add here.

## Assignments

**A1.** Derive both worked scores and both means. Explain why a Brier implementation dividing by three will disagree while possibly preserving rankings.

**A2.** Submit an independent `audit.py` and metrics JSON reproducing four model scores and all four bootstrap intervals. Add failure tests for duplicate IDs, unequal model populations and invalid probability sums. Check class order from known fixtures, not just sum-to-one assertions.

**A3.** Write a 250-word result. Include the public-minus-market sign, sample size, weighting, interval limitations and status of further tuning on these dates. Explain why the frequency model belongs in the comparison.

Mastery check: you can reproduce the number and explain why its uncertainty does not resolve missing receipt history or biased sampling.

Check your work with the [answer key](../answers/03_scoring.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
