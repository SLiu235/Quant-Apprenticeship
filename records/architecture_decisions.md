# Architecture Decisions

## Reference package decision — authored by mentor, not a learner assessment

Problem: provide a complete, inspectable integrated teaching example that runs locally.

Options: extend the empirical scripts directly; introduce services and a data platform; add a standard-library package alongside the existing reference library.

Decision: use a standard-library package with explicit component boundaries, synthetic fixtures, JSON artifacts and SQLite fill persistence.

Reason: permits reproducible offline runs without data subscriptions or installation; preserves the separate provenance of existing empirical studies.

Tradeoffs: toy market mechanics, no live model/broker, no full order recovery, limited risk model. Simplicity exposes the contracts but does not establish production readiness.

When to reconsider: a learner project has measured requirements for richer data, concurrency, latency, reliability or model capability.

## Blank learner entry

```text
Problem:
Options:
Decision:
Reason:
Tradeoffs:
When to reconsider:
Evidence:
```
