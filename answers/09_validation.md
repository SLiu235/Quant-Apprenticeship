# Lesson 9 answer key — Design walk-forward evaluation and a research ledger

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

1−.95^100≈.99407947, assuming independent null tests. The day 8 feature timestamp does not make its day 12 label known at day 10. Exclude that training label from a fit at day 10. For statistical split purity, also inspect overlap between its outcome interval and evaluation intervals; timestamp eligibility and dependence are related but distinct concerns.

## A2

Represent each label with start, end and available_at. At decision t, require available_at≤t. For a protocol forbidding overlapping outcomes across partitions, interval overlap occurs if max(start_a,start_b)≤min(end_a,end_b) for closed intervals; define endpoint convention explicitly. Test touching boundaries, disjoint intervals, same-day unavailable labels and timezone equivalence.

Nested scheme: within development history, use expanding inner training/validation folds for hyperparameters; outer later folds compare the model-selection procedures. Select the final procedure using only development results, freeze its retraining schedule and evaluate a new final period once. Do not use outer/final outcomes to revise candidate features while still calling those folds untouched. A small dataset may justify fewer comparisons rather than elaborate nesting with tiny cells.

## A3

All three ideas are development hypotheses now. Preserve the losing baseline entry. The sign reversal must be marked proposed-after-evaluation. Text already has an unfavorable saved result; a new representation is a new candidate. Stop after the declared comparison budget or if timing/coverage cannot support the question. Confirmation requires uninspected independently acquired later data and a frozen protocol; changing the random seed or splitting the same inspected dates differently does not qualify.

Repair: ask a reviewer to reconstruct how many chances the final rule had to look good. If the ledger cannot answer, repair it before reporting significance.
