# Lesson 2 answer key — Build a point-in-time information set

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

The first feature is usable at 09:25:05, so the 09:25:00 decision must exclude it; 09:25:06 may include it if all other dependencies are ready. Missing receipt should remain null with a separately named estimated availability field and an assumption tag. Reject it from a strict observed-receipt experiment, or explicitly run an assumption-dependent sensitivity study. Do not relabel estimates as observed timestamps.

## A2

Reference algorithm: validate unique `(document_id, version_id)`, parse aware availability timestamps, exclude records after cutoff, group by document, choose maximum eligible availability/version order under a defined tie rule. Raise on missing availability in this strict exercise and conflicting duplicate version IDs. Fixtures must return original A and document B at 09:25, revised A at 09:27. Test exact equality at cutoff and offset-equivalent timestamps as well. The project reference's simple `eligible` filter is deliberately smaller; your version selection is a required extension.

A dictionary keyed only by document ID before the as-of filter commonly destroys the original version. Filter versions before selecting the eligible maximum. Treat ambiguous timestamp ties as errors unless a provider sequence resolves them.

## A3

One plausible path is outcome → later attention → collection, with initial post characteristics also affecting attention. Conditioning on collection can connect post characteristics and outcomes without the desired mechanism. This diagram illustrates a possible bias; its sign is not established. Prospectively collect a predetermined universe of root posts and all eligible comments at fixed polling intervals, independent of eventual engagement; record receipts, edits, omissions and outages. Delay changes time eligibility, not the upstream inclusion process.

R2 warns about fit-time leakage; collection-conditioned sampling is an additional problem outside a standard ML pipeline. Repair by separating a row-validity checklist from a population-coverage checklist.
