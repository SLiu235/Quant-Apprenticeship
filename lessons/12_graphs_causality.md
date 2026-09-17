# Lesson 12 — Distinguish a discussion graph from knowledge propagation

Prerequisites: Lessons 2 and 10–11. Suggested effort: 5–7 hours, including the lab. Project: 4.

## Define what an edge means

A graph can encode reply-to, repost, co-mention, transaction or observed exposure. These relations are not interchangeable. A comment in the same thread is evidence of participation, not proof of reading the root, endorsing it or changing a trade because of it. Store edge type, direction, observation time, source and uncertainty. Missing edges may mean unobserved coverage rather than no connection.

A graph feature at t must use only eligible edges and node attributes. A graph embedding trained on the full future network can leak even if the final neighbor query is timestamp-filtered. Fit graph transformations on permitted history or use a clearly documented inductive procedure. Compare graph features to degree/activity controls so a claimed propagation effect is not simply “popular posts predict something.”

Association alone does not identify influence. Homophily can make similar traders read similar material and act similarly; a common news shock can drive both discussion and returns. In a causal graph, U→discussion and U→return produces association without discussion causing the return. Conditioning on eventual collection can introduce additional bias. R12 provides the exchangeability and selection framework.

## Worked counterexample

Suppose an earnings release makes 100 investors independently post and buy. A later observer sees dense co-discussion and aligned actions. Removing communication links in a drawing does not tell us what those investors would have done without the public release. To estimate a communication effect, define the intervention and address shared information, selection and interference. An actual randomized exposure design would be stronger, but market spillovers still complicate treatment/control interpretation.

The local graph comparison has an additional known collection problem: comments were sampled by eventual engagement. Its unfavorable or favorable loss difference would remain a biased discussion diagnostic. More elaborate graph neural networks cannot repair missing exposure observations.

## Lab procedure

1. Create a tiny temporal edge table with reply, co-mention and observed-exposure types; mark the last type synthetic unless actually observed.
2. Build counts using only edges available by cutoff. Add a future-edge mutation test.
3. Compare a graph feature with a root-text-only feature and an activity/degree control on the same observations.
4. Draw two alternative causal diagrams that generate the same observed association.
5. Read R12 on exchangeability and selection. Identify the assumption your archive cannot establish.

## Assignments

**A1.** Explain why the earnings counterexample does not identify peer influence. Define one precise causal estimand and its intervention.

**A2.** Implement temporal edge counts with edge-type separation and missing-coverage indicators. Test that future edges and future-fitted node attributes cannot alter earlier features.

**A3.** Write a 200-word empirical-feasibility decision for graph-IRL using this archive. List the extra observations needed for exposure, actions and state, and propose one useful noncausal study that remains possible.

Mastery check: every graph claim names an observed edge relation and separates predictive utility from a causal mechanism.

Check your work with the [answer key](../answers/12_graphs_causality.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
