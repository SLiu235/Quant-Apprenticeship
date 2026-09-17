# Lesson 10 — Define the NLP task before selecting a language model

Prerequisites: Lessons 7–9. Suggested effort: 5–7 hours, including the lab. Project: 4.

## Sentiment, claims and return forecasts are different labels

A post may be positive about a product but negative about its price, quote someone else's optimism, express sarcasm, or discuss an index rather than an issuer. Ticker strings can be ordinary words. Define entity resolution, target aspect, forecast horizon, assertion versus quotation and abstention before annotation. A model cannot compensate for inconsistent labeling instructions.

Separate three stages: extracting a documented claim, estimating its financial implication and forecasting a market outcome conditional on what was already priced. “Revenue grew” can be a true positive business statement while the stock falls because expectations were higher. Text-classification accuracy tests an annotation task; incremental market forecasting needs a matched price-only baseline and valid availability.

For annotation, keep an adjudicated reference set, an ambiguity policy and disagreement records. Measure class-conditional errors and coverage. Abstention can improve accepted-case accuracy by removing difficult cases; always report what fraction remains and whether abstention changes the trading population. Split near-duplicate posts and quoted copies as groups to avoid near-identical text in development and evaluation.

## Worked example

“MU revenue rose, but guidance is uncertain” receives our `mixed` label. A system returns `positive` with the exact quote “revenue rose.” The quote is real, yet the overall label misses the qualification. Another system invents “strong company growth” for an index-rebalance post. The first is a semantic error; the second also fails evidence grounding. Different tests must catch them.

## Lab procedure

1. Write a one-page annotation guide with five labels: positive, negative, neutral, mixed, abstain. Give inclusion/exclusion examples.
2. Run Project 4. Its text and cached responses are explicitly synthetic, including two deliberate errors; no real LLM was called.
3. Create 10 additional author-written adversarial examples, covering negation, quote attribution, ticker ambiguity, multilingual wording and duplicate text. Label before running any classifier.
4. Read a small permitted local post sample for data understanding without copying user handles into reports. Keep sampled IDs in a private/local audit mapping if needed.
5. Read R9's task and evaluation sections. Explain the transfer gap between financial sentiment labels and our response target.

## Assignments

**A1.** Reproduce Project 4's eligible count, grounding-valid count, accepted coverage and accepted accuracy. Explain the status of the post that appears one minute after the cutoff.

**A2.** Submit your annotation guide,10 fixtures and a confusion matrix for a lexical baseline. Add a separate abstention/coverage report and a paired-population plan for a market comparison.

**A3.** Design an ablation comparing market, market+lexical, market+frozen-encoder features. Specify entity handling, temporal document split, label policy and which data would remain uninspected.

Mastery check: you can locate whether an error came from entity matching, evidence extraction, interpretation or financial prediction.

Check your work with the [answer key](../answers/10_text_features.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
