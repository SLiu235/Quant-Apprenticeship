# AI quant research apprenticeship

**Professional research revision:** [critique and expectations](PROFESSIONAL_REVIEW.md) · [six research studios, new code labs and evidence standards](PROFESSIONAL_TRACK.md). The material below is a foundation library; independent original research and economic/system ownership require the professional-track evidence.

**Full apprenticeship pack:** [ten integrated modules, all code, projects, optional assessments and learning records](FULL_PACKAGE.md). This is the current entry point. The 24-lesson library below remains available for deeper study; its original prescribed sequence and pass rules are optional under the current [self-paced assessment policy](assessments/SELF_PACED.md).

A complete self-paced core course for a graduate with strong AI, mathematics, statistics and coding. Learn to turn a market mechanism into a reproducible experiment, assess statistical and economic evidence, and defend a research decision. Positive trading returns are not a passing requirement.

**Start with [the student guide](START_HERE.md).** The package contains 24 written lessons, 72 assignments with matching answer keys, eight integrated projects and runnable worked examples, primary readings, templates, grading/remediation and three explicitly simulated quant-CEO design reviews.

## Curriculum

Complete each group of three lessons, then its project. Effort estimates are in the lessons and projects; the full core is approximately 250–400 hours. Original workspace projects remain reference material. Student work belongs under `submissions/`.

| Stage | Written lessons | Integrated project |
|---|---|---|
| 1. Research validity | [1. Define what the experiment can establish](lessons/01_research_contract.md)<br>[2. Build a point-in-time information set](lessons/02_availability.md)<br>[3. Score forecasts and quantify dependent evidence](lessons/03_scoring.md) | [Project 1](projects/01_audit.md) |
| 2. Markets and execution | [4. Translate financial contracts into PnL](lessons/04_instruments.md)<br>[5. Replay a decision and account for fills](lessons/05_execution.md)<br>[6. Make calendars and changing sessions explicit](lessons/06_sessions.md) | [Project 2](projects/02_replay.md) |
| 3. Data and baselines | [7. Build a point-in-time market panel](lessons/07_data_pipeline.md)<br>[8. Make a simple model earn its complexity](lessons/08_baseline.md)<br>[9. Design walk-forward evaluation and a research ledger](lessons/09_validation.md) | [Project 3](projects/03_baseline.md) |
| 4. Text, LLMs and graphs | [10. Define the NLP task before selecting a language model](lessons/10_text_features.md)<br>[11. Evaluate retrieval and research agents as systems](lessons/11_llm_systems.md)<br>[12. Distinguish a discussion graph from knowledge propagation](lessons/12_graphs_causality.md) | [Project 4](projects/04_text.md) |
| 5. Models, risk and allocation | [13. Evaluate time-series models under regime change](lessons/13_time_series_ai.md)<br>[14. Forecast uncertainty and test calibration](lessons/14_risk_forecasts.md)<br>[15. Optimize a constrained portfolio and test its economics](lessons/15_portfolios.md) | [Project 5](projects/05_risk.md) |
| 6. RL, IRL and transfer | [16. Establish the support for a sequential decision policy](lessons/16_offline_rl.md)<br>[17. Fit a restricted utility model and test identification](lessons/17_inverse_rl.md)<br>[18. Challenge learned behavior under misspecification](lessons/18_transfer.md) | [Project 6](projects/06_behavior.md) |
| 7. Engineering and operation | [19. Make an experiment independently reproducible](lessons/19_research_software.md)<br>[20. Spend compute on measured research bottlenecks](lessons/20_compute.md)<br>[21. Operate a paper research system and recover from failures](lessons/21_operations.md) | [Project 7](projects/07_operations.md) |
| 8. Independent research and career | [22. Design a bounded independent research study](lessons/22_capstone_protocol.md)<br>[23. Run an independent review and assess economic relevance](lessons/23_replication_review.md)<br>[24. Defend your work and build a research practice](lessons/24_research_career.md) | [Project 8](projects/08_capstone.md) |

## What is included

- **Teaching and solutions:** each lesson contains explanation, mathematics, a worked example, a lab procedure, A1–A3 and a linked answer key. [Supplemental numerical solutions](reference/solutions.py) support the implementation exercises.
- **Worked research:** eight local reference programs and saved outputs, including a [complete negative-result capstone memo](projects/08_worked_memo.md).
- **Independent progress:** [setup and troubleshooting](guides/SETUP.md), [mastery rubric](assessments/MASTERY.md), [reading library](guides/READINGS.md), [glossary](guides/GLOSSARY.md), and [data/compute paths](guides/DATA_AND_COMPUTE.md).
- **Reusable artifacts:** [research contract](templates/research_contract.md), [experiment ledger](templates/experiment_ledger.md), [model card](templates/model_card.md), [research memo](templates/research_memo.md), and [portfolio index](templates/portfolio_index.md).
- **Design reviews:** [round 1: theory-first](design/01_theory_first.md), [round 2: project ladder](design/02_project_ladder.md), and [round 3: complete research workflow](design/03_research_desk.md). These are editorial simulations, not statements by actual executives.

## Evidence and scope

The empirical examples use existing real vendor bars for four Nasdaq-listed issuers and the recent 2025–February 2026 Reddit/price pilot. Local prices reach September 2026; the social archive does not. The saved evaluation is already inspected. Synthetic execution, cached NLP and IRL examples are clearly labeled; no live LLM, investor-intent recovery, current social stream or overnight execution performance is claimed.

The training covers research practice, market contracts, information clocks, time-series/ML evaluation, NLP/LLM systems, graphs/causality, risk/optimization, offline RL/IRL, performance engineering and paper operations. It provides a core foundation and explicit specialist paths, not a guarantee of employment, profitable strategies or mastery of every quant role.

## Verified release

All eight worked examples execute locally, deterministic outputs reproduce, and 16 tests pass. [Verification record](outputs/verification.json) includes runtime versions and code/data hashes; [test log](outputs/tests.log) records the checks. [Build and review record](BUILD_STATUS.md) maps requirements to completed artifacts. The verification distinguishes numerical/software evidence from pedagogical and market-validity judgments.

To reproduce the release checks:

```bash
cd /Users/dexter/Desktop/Projects/Quant/AIQuantApprenticeship
../QuantTimeLearn/.venv/bin/python -m reference.verify
```
