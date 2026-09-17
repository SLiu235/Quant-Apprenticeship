# Self-assessment, remediation and graduation

**Current policy:** all routine diagnostics and scoring in this reference rubric are optional. Use the [self-paced assessment policy](SELF_PACED.md) and the [ten integrated worksheets](../FULL_PACKAGE.md). The original pass/graduation language below does not automatically gate progress or certify competency.

Progress depends on evidence, not elapsed weeks or a profitable backtest. A mentor is optional for moving through this package. External review is valuable because self-review has blind spots; if none is available, do a separate review pass after a break and label it self-review.

## Entry diagnostic

Before Lesson 1, answer these without a key: (1) derive a least-squares gradient; (2) explain conditional expectation versus a realized outcome; (3) compute −log(.5); (4) write a Python assertion for a probability vector; (5) explain why a split is different from a random seed. The [diagnostic key](DIAGNOSTIC_KEY.md) gives answers and targeted refreshers. Strong AI/math students should not spend weeks repeating elementary material; use the diagnostic to locate gaps.

## Lesson scoring

Each lesson has A1, A2 and A3, worth 0–4 points each.

| Score | Evidence |
|---|---|
| 0 | Missing, fabricated or answers a different question |
| 1 | Some correct terminology but central reasoning or implementation wrong |
| 2 | Mostly correct with a material missing check, assumption or explanation |
| 3 | Correct and complete, with reproducible evidence where required |
| 4 | Correct, complete and independently challenged with a changed fixture or alternative derivation |

Pass a lesson at 9/12 with no assignment below 2 and no unresolved gate failure. Read the matching answer key after attempting it. Keep original work, your self-score, the discrepancy and a corrected version. Then solve a changed example without looking at the solution. For an open-ended implementation, the key gives expected invariants and algorithms; multiple implementations and honest negative results can receive full credit.

Hard gates: future information used as historical; target/state claimed observed when absent; fabricated or mislabeled real/model outputs; incompatible comparison populations; incorrect economic units or cash accounting; unsupported causal/participant/production claims. Repair a gate regardless of total points. A limitation correctly identified and scoped is not itself a gate failure.

## Project rubric

| Dimension | Weight | Full-credit evidence |
|---|---:|---|
| Contract and mechanism | 15 | Observable target, population, comparison, falsifiable decision |
| Data and availability | 25 | Provenance, selection, clock/version lineage, exclusions |
| Evaluation | 25 | Comparable baselines, chronological selection, dependence, all variants |
| Economics and scope | 15 | Correct units/costs/capacity or an explicit limit on economic claims |
| Implementation | 10 | Reproducible code, independent checks, focused failure tests |
| Communication | 10 | Clear result, limitations and a justified next-information choice |

Score each dimension 0–4 using the lesson descriptions; total=Σ(weight×score/4). Pass at 80/100 with no dimension below 2 and no hard-gate failure. Show the evidence link next to each score. For a synthetic or feasibility project, economic full credit means accurate scope plus a concrete acquisition/evaluation path, not invented PnL.

## Remediation map

| Failure | Repair activity | Retest |
|---|---|---|
| Metric mismatch | Hand-score a three-class vector; inspect class order and weights | Changed probability vector with independently calculated answer |
| Timing leak | Draw receipt/feature/label intervals | Future-revision mutation and boundary fixture |
| Selected population mistaken for market | Enumerate inclusion rules and missing cases | Explain one excluded issuer/day and its inferential consequence |
| Excess model search | Reconstruct ledger and mark exposed dates development-only | Freeze a bounded next experiment on genuinely new evidence |
| Confused PnL/forecast/utility | Rewrite the claim ladder with necessary observations | Defend one unsupported claim and its required data |
| Execution/accounting error | Replay fills/cancel requests by hand | Partial fill, duplicate, overfill and restart fixtures |
| Unsupported causal claim | Draw common-cause/selection alternatives | Define intervention and evidence needed to distinguish them |
| Performance claim without measurement | Establish CPU reference and timing boundary | Repeat benchmark with correctness and end-to-end profile |

## Project review cadence

Complete each group of three lessons, then integrate its project. The sample shows a complete core result; the student project deliberately extends it. Budget the project effort in addition to lesson effort. At review, answer: What did I measure? What was knowable then? What did the baseline do? What could explain the result? What would I do next and why?

## Graduation evidence

Complete all 24 lessons and eight projects, pass the capstone rubric, and assemble the portfolio index. Defend a numerical derivation, an information clock, an implementation failure and a negative decision without reading the keys. Your final scope statement must name specialist gaps and the next project to close one of them.

This is a substantial core apprenticeship, approximately 250–400 hours depending on prior familiarity and capstone data work. The estimates are planning aids, not deadlines or employment guarantees. Passing demonstrates the documented competencies; it does not certify mastery of every asset class, infrastructure stack or market regime.
