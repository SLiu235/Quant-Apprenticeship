# Lesson 22 — Design a bounded independent research study

Prerequisites: Lessons 1–21. Suggested effort: 6–10 hours, including the lab. Project: 8.

## Independence begins before the final experiment

Choose a mechanism whose evidence you can obtain. A capstone does not need a profitable strategy; it must produce a defensible research decision. The existing negative social pilot is the worked example, not an untouched dataset for a new claim. Your capstone should either obtain independently uninspected data or explicitly study reproducibility, sensitivity or feasibility without pretending to confirm alpha.

Use a claim ladder. At the first level, validate data timing and measurement. Next, compare predictive information. Then assess a specified decision with costs and constraints. Only add participant utility or causal propagation when the required observations exist. Each stronger claim should name its extra assumptions and a failure condition.

Choose one primary question. “Use agents, graphs, IRL and overnight trading” is a collection of tools, not a research design. A feasible question could be whether a prospectively frozen text representation improves a preopen probability forecast over a price-only baseline on a specified universe. A different question could test whether an observed order-flow state improves a passive-fill forecast in a particular session. They need different data and cannot be merged by renaming the target.

## Worked protocol decision

The sample capstone retains the public-minus-market equal-date NLL comparison and recommends not promoting the model. It explicitly declines IRL and trading-PnL claims. Its next experiment is prospective acquisition with actual receipt/version logging and a frozen baseline. That experiment first resolves whether a valid paired panel can be built; it does not guarantee that a richer text feature will improve returns.

## Lab procedure

1. Choose a capstone track in Project 8: response prediction, execution/behavior with adequate logs, or a rigorous feasibility/reproduction study.
2. Complete the protocol template, source manifest and candidate budget before acquiring evaluation outcomes.
3. Draw the dependency graph from source receipts to feature completion, decision, fill/outcome and label arrival.
4. Specify primary/secondary metrics, date weighting, uncertainty, costs where applicable, exclusions and stop rules.
5. Read the relevant R3/R12/R17 source depending on your claim. Explain one condition where its method would not transfer to your data.

## Assignments

**A1.** Write a 300-word protocol abstract including claim, population, data tier, decision clock, baseline, evaluation and rejection condition.

**A2.** Produce a complete acquisition/analysis plan with schema, manifest, split algorithm, model budget, test cases and estimated resource use. Execute the plan on a small explicit fixture to catch mechanical failures before fresh data.

**A3.** Pre-mortem your study: list three plausible reasons it could mislead, the diagnostic for each and whether the current data can resolve it. Choose one next experiment rather than three simultaneous changes.

Mastery check: a reviewer can state what finding would reject the hypothesis and what finding would still be insufficient for deployment.

Check your work with the [answer key](../answers/22_capstone_protocol.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
