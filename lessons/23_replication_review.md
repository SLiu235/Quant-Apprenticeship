# Lesson 23 — Run an independent review and assess economic relevance

Prerequisites: Lesson 22. Suggested effort: 6–10 hours, including the lab. Project: 8.

## A research review should be able to change the decision

A reviewer needs the contract, exact inputs, code, predictions, uncertainty calculation and economic interpretation. Reproducing a table is necessary but not enough: challenge whether the table measures the claimed object. Separate correctness, statistical evidence, economic usefulness and operational feasibility. A result can pass one and fail another.

Use paired comparisons and preserve unsuccessful variants. Inspect regime/session slices as diagnostics with sample counts, not as new primary tests chosen because they look good. For overlapping forecasts, resampling should respect the relevant dependence. For trading claims, assess turnover, borrowing/financing, spreads, impact, unfilled orders, capacity and benchmark exposure under explicitly estimated or stipulated assumptions.

A threshold “t-stat>2” does not excuse a large hidden search, just as “NLL improved” does not justify unlimited inference spend. Decision relevance depends on effect size relative to cost and uncertainty. Consider the value of further information: if the plausible improvement is tiny while data acquisition is expensive and timing remains unobservable, stopping can be the best research choice.

## Worked committee objection

A report says: “The graph model learned investor behavior because its loss improved on one issuer.” The reviewer asks whether this was prespecified, how many issuers/models were inspected, whether the graph samples all discussion, and whether actions were observed. Even a correct favorable slice would not identify investor utility. The appropriate revision narrows the claim and records the slice as exploratory rather than rebranding it as the main finding.

## Lab procedure

1. Reproduce your capstone from a clean process without reading your development notes.
2. Compare artifacts against the frozen contract and list all deviations.
3. Run an adversarial review focused separately on timing, population, statistics and economics. AI assistance may propose objections; verify each against files.
4. Write a response table: objection, evidence, fix or limitation, effect on conclusion.
5. Read R4 again with your actual candidate ledger in view. Count the research choices that your headline test omits.

## Assignments

**A1.** A model claims 3 bps gross mean with turnover 1.5 and 4 bps one-way costs. Compute estimated net and explain the meaning of a break-even cost.

**A2.** Produce a replication report and at least five concrete review findings tied to your artifacts. Fix correctness defects, rerun affected checks and preserve honest limitations.

**A3.** Write a go/revise/stop decision with one primary evidence statement, one economic constraint and one next-information choice. Respond to the graph-issuer objection above.

Mastery check: your review can recommend stopping despite technically correct code, and your response distinguishes a repaired defect from a remaining limitation.

Check your work with the [answer key](../answers/23_replication_review.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
