# AI-native investment apprenticeship — full package

**Professional revision, September 14:** start with the [critical review](PROFESSIONAL_REVIEW.md) and [professional research track](PROFESSIONAL_TRACK.md). Six research studios now connect the foundation to original hypotheses, data diligence, actual predictive AI, economic value and independent ownership. New executable labs provide committed experiment budgets, trained neural/linear comparisons, matched portfolio stress scenarios and AI-output evaluation. This pack supports the work; completing its reference examples does not establish professional mastery.

This is the complete learning-pack index: ten integrated modules, ten build projects, runnable shared code, optional assessments and keys, plus the existing 24 deeper lessons and eight worked projects. Everything is available now; study one module at a time at your own pace. Assessment happens when you request it, submit work, ask about readiness, or when a blocking misconception or major integration milestone needs verification. There is no automatic promotion.

## Start or run everything

Open a terminal:

```bash
cd /Users/dexter/Desktop/Projects/Quant/AIQuantApprenticeship
python3 -m apprentice_system.run --stage 10 --output outputs/integrated
python3 -m unittest discover -s tests -p test_integrated.py -v
```

The integrated reference requires Python 3.11+ and only the standard library. `--stage N` runs stages 1 through N. Results are JSON files; the code makes no network calls and has no broker connection. Start your learning with [Module 1](modules/01_research_environment.md), regardless of whether you run all the worked examples first.

For the existing empirical/ML examples, use the workspace runtime with NumPy/SciPy and the existing sibling data:

```bash
../QuantTimeLearn/.venv/bin/python -m reference.run --project all --output outputs/legacy_check
../QuantTimeLearn/.venv/bin/python -m unittest discover -s tests -v
```

See [setup](guides/SETUP.md) for an independent environment. Running examples verifies the software under its stated assumptions; it does not demonstrate your independent competency.

## Integrated modules, projects and code

| Stage | Module and teaching notes | Build project | Runnable component | Optional assessment |
|---|---|---|---|---|
| 1 | [Trustworthy research run](modules/01_research_environment.md) | [Project 1](projects/integrated/01_research_environment.md) | [Contracts and identity](apprentice_system/core.py) | [Worksheet 1](assessments/integrated/01_research_environment.md) |
| 2 | [Point-in-time data](modules/02_point_in_time_data.md) | [Project 2](projects/integrated/02_point_in_time_data.md) | [Data and features](apprentice_system/data.py) | [Worksheet 2](assessments/integrated/02_point_in_time_data.md) |
| 3 | [Signal research](modules/03_signal_research.md) | [Project 3](projects/integrated/03_signal_research.md) | [Walk-forward research](apprentice_system/research.py) | [Worksheet 3](assessments/integrated/03_signal_research.md) |
| 4 | [Portfolio construction](modules/04_portfolio_construction.md) | [Project 4](projects/integrated/04_portfolio_construction.md) | [Targets and orders](apprentice_system/portfolio.py) | [Worksheet 4](assessments/integrated/04_portfolio_construction.md) |
| 5 | [Risk and attribution](modules/05_risk_attribution.md) | [Project 5](projects/integrated/05_risk_attribution.md) | [Scenarios and P&L](apprentice_system/risk.py) | [Worksheet 5](assessments/integrated/05_risk_attribution.md) |
| 6 | [Execution and microstructure](modules/06_execution_microstructure.md) | [Project 6](projects/integrated/06_execution_microstructure.md) | [Fills, costs, ledger, TWAP](apprentice_system/execution.py) | [Worksheet 6](assessments/integrated/06_execution_microstructure.md) |
| 7 | [Production pipelines](modules/07_production_pipelines.md) | [Project 7](projects/integrated/07_production_pipelines.md) | [Artifacts and event store](apprentice_system/pipeline.py) | [Worksheet 7](assessments/integrated/07_production_pipelines.md) |
| 8 | [AI research copilot](modules/08_ai_research_copilot.md) | [Project 8](projects/integrated/08_ai_research_copilot.md) | [Temporal retrieval baseline](apprentice_system/copilot.py) | [Worksheet 8](assessments/integrated/08_ai_research_copilot.md) |
| 9 | [Monitoring and incidents](modules/09_monitoring_observability.md) | [Project 9](projects/integrated/09_monitoring_observability.md) | [Invariant alerts](apprentice_system/monitoring.py) | [Worksheet 9](assessments/integrated/09_monitoring_observability.md) |
| 10 | [Integrated paper system](modules/10_integrated_paper_system.md) | [Project 10](projects/integrated/10_integrated_paper_system.md) | [Orchestrator and replay](apprentice_system/run.py) | [Worksheet 10](assessments/integrated/10_integrated_paper_system.md) |

Every module contains objective, prerequisites, core knowledge, mental models, worked example, implementation, failure cases, debugging exercise, decision exercise and completion criteria. Each assessment links to a separate hint/answer file. [Test code](tests/test_integrated.py) provides executable examples of correctness and failure checks.

## Architecture and dependencies

```text
Versioned data → features frozen at decision time → matured-label research
    → forecasts with descriptive uncertainty → constrained portfolio targets
    → risk checks → signed orders → partial-fill simulator → cash and positions
    → independent P&L reconciliation → attribution → monitoring → research decisions

Artifact manifests and durable events support the full chain.
Temporal evidence retrieval supports research; it cannot place orders.
```

Learn research specification and reproducible engineering first; then information timing and data; then validation; then capital allocation, risk and execution; then operational recovery and evaluated AI. Risk, market mechanics, observability and professional communication begin with the first component rather than waiting for their dedicated module.

The [professional architecture](PROFESSIONAL_TRACK.md#architecture-revision) adds research commitments before model selection and independent challenge before prospective claims. The replay now compares cash/equal-weight/signal policies and separates overnight, intraday and execution P&L. [New lab commands and saved results](PROFESSIONAL_TRACK.md#run-the-new-labs) make those checks inspectable.

## Existing deeper lessons and eight worked projects

The [24-lesson library](README.md#curriculum) remains available, including its 72 assignments and 24 answer keys. Its old sequence is a library organization, not an obligation to complete assessments after every section.

| Worked project | Main use in the integrated apprenticeship | Code |
|---|---|---|
| [Audit a public-signal study](projects/01_audit.md) | Modules 1–3: empirical evidence, information clocks, dependence | [p01_audit.py](reference/p01_audit.py) |
| [Execution replay](projects/02_replay.md) | Modules 5–6: passive queue and shortfall | [p02_replay.py](reference/p02_replay.py) |
| [Research baseline](projects/03_baseline.md) | Module 3: simple empirical model and validation | [p03_baseline.py](reference/p03_baseline.py) |
| [Text research](projects/04_text.md) | Module 8: cached model evaluations and evidence checking | [p04_text.py](reference/p04_text.py) |
| [Risk and allocation](projects/05_risk.md) | Modules 4–5: covariance shrinkage and optimization | [p05_risk.py](reference/p05_risk.py) |
| [Behavioral models](projects/06_behavior.md) | Optional research extension: RL/IRL identification | [p06_irl.py](reference/p06_irl.py) |
| [Paper operations](projects/07_operations.md) | Modules 7–9: failure states and measured computation | [p07_operations.py](reference/p07_operations.py) |
| [Research committee](projects/08_capstone.md) | Module 10: independent research decision | [p08_committee.py](reference/p08_committee.py) |

[Supplemental numerical solutions](reference/solutions.py) · [Worked negative-result memo](projects/08_worked_memo.md) · [Additional specialist build briefs](guides/SPECIALIST_LABS.md).

## Assessments, templates and learning records

[Self-paced assessment policy and rubric](assessments/SELF_PACED.md). You may use the answer keys independently or submit work for review. The assessment files are available now; they do not trigger an assessment.

Start from the [research contract](templates/research_contract.md), [research memo](templates/research_memo.md), [experiment ledger](templates/experiment_ledger.md) and [model card](templates/model_card.md).

Maintain the five concise records:

- [Skill Gap Ledger](records/skill_gap_ledger.md)
- [Decision Journal](records/decision_journal.md)
- [Bug Journal](records/bug_journal.md)
- [Research Journal](records/research_journal.md)
- [Architecture Decisions](records/architecture_decisions.md)

Store independent work under `submissions/integrated_XX/`. Do not replace your first attempt with a solution; preserve both when learning from a review.

## What is complete and what you build

All ten teaching modules, project briefs, optional assessments, answer keys and the ten-stage reference pipeline are supplied. Independent project extensions remain learner work. The integrated reference is an offline teaching implementation, not a production trading platform. The AI component is a deterministic retrieval baseline; no live model performance is claimed. [Scope matrix and source notes](guides/INTEGRATED_SCOPE.md) distinguish implemented behavior, existing advanced references and further build requirements. [Verification record](outputs/integrated_verification.json) records checks performed for this pack.

The [professional verification record](outputs/professional_verification.json) supersedes the earlier check counts for this revision. The added predictive-model lab performs actual local training; the research assistant remains a deterministic baseline with authored evaluation fixtures. Live generative-model evaluation and prospective market results are not claimed.

The archive contains the written pack, code and saved reports. The integrated example runs independently. The older empirical projects still require the sibling `BehaviorIRL` data/code listed in the setup guide; those source datasets and third-party Python environments are not copied into the archive.
