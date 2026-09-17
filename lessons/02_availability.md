# Lesson 2 — Build a point-in-time information set

Prerequisites: Lesson 1. Suggested effort: 4–5 hours, including the lab. Project: 1.

## The data object has more than one clock

Event time describes when something happened. Publication time describes a public release. Receipt time describes arrival at your system. Revision time describes an edit. A feature also needs computation time; a model needs a training completion time. Define usable_at = max(required input receipt times, model_ready_at) + feature/inference latency. A backtest decision may use a feature only if usable_at ≤ decision_at.

Historical archives often expose only creation time. Substituting creation+60s is an assumption, not a recovered receipt log. Store both the observed clock and the assumed clock so a later analyst can challenge the substitution. Use timezone-aware timestamps and UTC internally; preserve exchange local time and session identifiers for interpretation.

“Available by t” is a row constraint. It does not repair the population sampled. In the recent archive, comments were collected for threads that eventually exceeded ten replies. Market outcomes may affect later attention, which affects collection. Filtering the retained comments to those created before t cannot recover uncollected comments or remove selection at the thread level. Missing comments mean unknown coverage, not zero discussion.

## Worked example

A post is published at 09:24:30 ET, received at 09:24:58, embedded at 09:25:03 and classified at 09:25:05. It is unavailable for a 09:25:00 decision even though its creation precedes the cutoff. If a second source arrives at 09:24:50, combining sources still waits for the slower necessary input. A revised text first downloaded tomorrow cannot be treated as today's original merely because its post ID is stable.

## Lab procedure

1. Inspect one record each in the local prepared `responses.jsonl`, `events.jsonl` and `evidence.jsonl`. Join by explicit identifiers, not row number.
2. Make a timeline with prior state availability, post creation, assumed post availability, decision, outcome and label availability. Label every assumption.
3. Implement `asof(records, cutoff)` on author-written records containing UTC timestamps and values. Do not expose targets in the feature object.
4. Add an edited record with the same document ID but a later version availability. Return the most recent eligible version, not the most recent downloaded version.
5. Read R2's data-leakage section and the local source audit linked in the reading library. Explain why preprocessing pipelines are necessary but insufficient.

## Assignments

**A1.** Calculate usability for the worked timeline and for a decision at 09:25:06. Explain how to represent a missing receipt time without inventing evidence.

**A2.** Implement and test a version-aware as-of join on three fixtures: original at 09:20, revision at 09:26, another document at 09:24. At 09:25 return the original and the other document. Add a missing-clock case and a duplicate-version case with an explicit reject policy. Submit code and test output.

**A3.** Draw a causal selection diagram in text with market outcome, eventual attention and collection. Propose prospective acquisition that addresses coverage. Explain why adding a 24-hour delay alone does not solve it.

Mastery check: you can reject a future revision while retaining the correct earlier version, and can explain a selection defect that passes every row-time assertion.

Check your work with the [answer key](../answers/02_availability.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
