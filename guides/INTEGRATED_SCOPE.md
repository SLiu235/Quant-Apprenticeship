# Reference scope, assumptions and sources

The September 14 [professional revision](../PROFESSIONAL_TRACK.md) adds executable research controls and real-data model comparisons. The original rows below describe the foundation; implemented additions are listed next.

## Implemented professional additions

| Component | Implemented behavior | Boundary |
|---|---|---|
| ExperimentBook | Committed protocols, reserved/failed trial budget, selection lock, exposure record, replay-safe identities | Local bookkeeping, not protection against hidden trials or direct file access |
| validation.py | Matured-label eligibility and paired equal-date moving-block intervals | Conditional descriptive inference; not a multiple-testing correction |
| model_lab.py | Actually trained ridge/ablated-ridge/MLP comparisons, zero baseline, train-only scaling, validation checkpointing | Selected real snapshots already inspected; no prospective or executable-alpha claim |
| frontier.py | 18 shared-setting policy/capital/cost scenarios; research-lock demonstration | Stipulated market costs, not measured capacity; policy risk exposures differ |
| ai_evaluation.py | Output/case pairing, evidence, labels, abstention, temporal provenance, resource and tool-request reporting | No live model calls; provided authored cases are not production evaluations |
| paper_replay | Scheduled-clock validation, duplicate rejection and reconciled overnight/intraday/cost attribution | Carried exposure remains; final inventory is still marked without liquidation |

## Implemented versus learner extension

| Area | Runnable reference | Independent extension or specialist work |
|---|---|---|
| Reproducibility | Source/data hashes, config identity, deterministic CLI | Config schemas, independent reproduction, package distribution |
| Data | Versioned synthetic bars, timestamp checks, as-of feature selection | SQL/Parquet adapters, membership, corporate actions, missing/stale policies |
| Research | Expanding scalar regression; zero/persistence loss comparisons | Rolling windows, interval purging, panel/factor experiments, multiple-testing controls |
| Portfolio | Capped long-only conviction, cash residual, integer-share deltas | Turnover-aware optimizer, long/short, robust views, borrow and financing |
| Risk | Named linear shocks, concentration checks, exact cash/price P&L identity | Factor exposures, calibrated risk, dividends/corporate actions, margin |
| Execution | Signed partial IOC fills, stipulated spread/impact, TWAP slices, shortfall | Persistent order lifecycle, passive queue/cancel races, calibrated TCA, volume-forecast schedules |
| Pipelines | Content-addressed artifacts and transactional SQLite fill replay | Full order/intent recovery, model activation, crash injection, deployment/rollback |
| AI | Temporal lexical retrieval, abstention, quote evidence validation | Evaluated live model adapter, embeddings/reranking, semantic faithfulness, justified agents |
| Monitoring | Freshness, finite state, exposure and P&L invariant checks | Stateful incident management, drift, alerts, latency/cost monitoring |
| Integration | Ten cumulative stages, restart and accounting checks | Independent baseline portfolios, empirical prospective evaluation and operational review |

The existing `reference/` programs add empirical scoring, numerical optimization, cached NLP, restricted IRL and a passive queue example. Their documented limitations still apply.

## Synthetic market and accounting assumptions

The fixture invents AAA, BBB and CCC prices. Its weekday list is not an exchange calendar. Times are explicitly UTC and are not assertions about any real market's hours. The reference uses no corporate actions, dividends, tax, borrow, funding, leverage, margin or FX conversion. Initial capital is a teaching parameter, not a recommendation.

At 15:55, features and sizing prices come from prior available bars. At 16:00 the simulator observes an execution quote and uses realized interval volume to cap a fill. This is a stipulated ex-post fill rule. It is not a realizable forecast-volume scheduling algorithm. Target weights can differ from filled weights. The allocator leaves cash and does not claim to solve the full portfolio objective.

End-of-session marks define equity. P&L includes carried holdings' movement as well as new trades. Forecast targets are intraday, so total portfolio P&L cannot be attributed solely to those forecasts. Final inventory is marked without liquidation or exit costs. Module 10 explicitly asks you to align horizons or isolate the exposures. The program stops on a simulated infeasible fill; a real economic fill cannot be wished away and would require reconciliation and incident handling.

SQLite preserves fill identities and ordering for local replay. It does not recover open exchange orders or establish network-wide exactly-once behavior. Atomic no-overwrite file publication prevents readers from seeing a half-written artifact in ordinary operation; power-loss guarantees, directory durability and distributed filesystems require additional analysis.

The lexical copilot quotes eligible documents. It is not an LLM, does not perform semantic inference, does not certify source truth and cannot submit orders. Its small fixture checks are software examples, not estimates of production accuracy.

## Targeted primary readings

These sources inform specific extensions, not a requirement to repeat coursework:

- [scikit-learn: common pitfalls and leakage](https://scikit-learn.org/stable/common_pitfalls.html): use when auditing where preprocessing is fitted. Learned transformations must be fitted within the relevant training data.
- [Almgren and Chriss, Optimal Execution of Portfolio Transactions](https://www.smallake.kr/wp-content/uploads/2016/03/optliq.pdf): original research paper, hosted as a PDF mirror. Use for the tradeoff between execution cost and uncertainty while waiting. The toy impact formula in this package is not an implementation or calibration of the paper's complete model.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): use to frame measurement and risk ownership for an AI component. This package does not claim conformance or certification.

The existing [reading library](READINGS.md) provides further sources for deeper lessons. Current market rules, instrument specifications, feed fields, costs and provider APIs must be checked against primary documentation when you implement a real-data adapter; the synthetic fixtures do not establish those facts.
