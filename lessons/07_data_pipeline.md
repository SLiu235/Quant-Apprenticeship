# Lesson 7 — Build a point-in-time market panel

Prerequisites: Lessons 1–6. Suggested effort: 5–7 hours, including the lab. Project: 3.

## A matrix is the end of a data pipeline

Security symbols are labels, not permanent identities. An issuer can change ticker; a share class can change economics; an index can add and remove constituents. A panel assembled from today's survivors conditions on future survival. Missing pre-listing prices are not zeros, and a delisting should not silently remove a losing position.

Represent security identity, vendor mapping, effective dates, availability dates and corporate actions explicitly. Separate raw immutable snapshots from normalized events, features, labels and model outputs. Each layer should name its parents and content hashes. Reproducibility means recovering what was actually used, including exclusions; downloading today's revised history is not enough.

Price adjustment requires purpose. A split-adjusted series can support continuity, while executed dollars use contemporaneous prices and quantities. A total-return series includes distributions that must not be added again as cash. Our reference uses same-day close/open returns to avoid silently attributing overnight split jumps to intraday returns, but that choice does not certify every vendor field or remove selection bias.

## Worked example

Stock A has price 100 before a 2:1 split and 50 after it. Raw close-to-close return appears−50%, although two shares now replace one. A correct holding ledger has unchanged value absent other moves. If stock B begins trading after your start date, filling earlier missing bars with its first observed price creates fictitious investability and flat returns.

The course has 394 common dates for four selected issuers; requiring all four further changes the sample. That is acceptable for a transparent software exercise, not a claim to a point-in-time Nasdaq universe. Daily prices extend to September 9, 2026 locally; the paired social pilot ends February 2026. Do not call those two coverages the same dataset.

## Lab procedure

1. Read `reference/common.py:price_panel` and each source hash in the Project 3 output. Inspect the raw Yahoo field structure.
2. Produce a coverage report per security before taking the common-date intersection: first/last date, missing/invalid bars and duplicate dates.
3. Design tables for raw observations, security mappings and corporate actions, with effective_at and available_at.
4. Reconstruct one feature row from raw inputs and compare its hash and timestamp lineage.
5. Read R2 and R3. Contrast our selected four-stock exercise with an empirical asset-pricing panel.

## Assignments

**A1.** Explain and calculate the split example. State how total-return data changes dividend accounting.

**A2.** Build the coverage report and a manifest recording source, retrieval snapshot, hash, adjustment convention, license status and exclusions. Add a failing duplicate-date fixture and never forward-fill pre-listing bars.

**A3.** Design a point-in-time universe query for “securities eligible as of decision t.” Explain which fields this workspace lacks and what acquisition would be necessary before a broad-market claim.

Mastery check: another researcher can trace one prediction to specific raw records and understand why another security/date was excluded.

Check your work with the [answer key](../answers/07_data_pipeline.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
