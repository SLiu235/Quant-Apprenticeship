# Professional AI-quant research track

[Critical review](PROFESSIONAL_REVIEW.md) · [Foundation modules and code](FULL_PACKAGE.md) · [Evidence rubric](assessments/PROFESSIONAL_EVIDENCE.md)

The ten foundation modules remain. This revision changes the work expected from them: each component must support an original, falsifiable investment problem and an accountable research decision. The studios below are integrated research milestones, not six new exams or a calendar. Begin each when the prerequisite evidence is ready. Assessment remains opt-in or tied to submitted work/readiness/necessary milestone verification.

## What I would expect beyond technical literacy

1. **Problem selection.** Identify a useful question before choosing the model. Explain the mechanism, market belief, competing interpretation and information advantage. Prioritize experiments by their ability to change a decision.
2. **Data judgment.** Understand what a dataset observes, what it misses, how it was selected and revised, and whether its use and historical timing support the proposed experiment. Reject attractive but unusable data.
3. **Independent science.** Reproduce a result, challenge it, log the search, perform informative ablations and make an original extension. Distinguish uncertainty from a convenient story about a regime.
4. **Deep model competence.** Understand representations, objectives, optimization, generalization and inference. Be able to diagnose a gradient, learning curve or deployment mismatch, and modify a model where the problem warrants it.
5. **Economic conversion.** Connect a prediction to expected payoff, marginal portfolio value, liquidity, signal decay, opportunity cost, capacity and an exit decision. A strong forecast can still deserve zero capital.
6. **AI-assisted research ownership.** Use AI to accelerate reading, coding and experiment analysis while personally verifying evidence. Count AI-generated searches and prompts as part of research selection. Separate generated answers, code execution and authority to take actions.
7. **System reliability.** Treat bad clocks, changed schemas, retries, stale models and reconciliation failures as part of the research domain. Know which failures invalidate the result and which merely delay it.
8. **Depth and collaboration.** Build exceptional depth in one market/mechanism, and communicate across research, PM, engineering and execution boundaries. Another person should be able to challenge and reproduce your work without reconstructing your intentions.

These are professional expectations proposed for this apprenticeship, informed by the sources in the review; they are not universal hiring criteria or a guarantee of a role.

## The six research studios

| Studio | Enter from | Evidence produced | Runnable support |
|---|---|---|---|
| [1. Edge and data advantage](professional/01_edge_and_data.md) | Modules 1–2 | Investment hypothesis, counter-thesis, data diligence, experiment priority | Contract and data validation |
| [2. Replication and original research](professional/02_research_discovery.md) | Modules 2–3 | Replication, one original extension, search log and falsification | [Experiment book](apprentice_system/research_control.py), [validation](apprentice_system/validation.py) |
| [3. Predictive AI and representation](professional/03_predictive_ai.md) | Modules 3, 7 | Actual trained models, ablations, learning/compute diagnosis | [Real-data model lab](apprentice_system/model_lab.py) |
| [4. Portfolio value and execution](professional/04_economic_value.md) | Modules 4–6 | Matched baselines, exposure/horizon attribution, capacity/exit study | [Replay](apprentice_system/run.py), [18-scenario lab](apprentice_system/frontier.py) |
| [5. Accountable AI research workflow](professional/05_ai_research_workflow.md) | Modules 7–8 | Measured AI value, evidence audit, contamination and failure cases | [Structured-output evaluation](apprentice_system/ai_evaluation.py) |
| [6. Independent ownership and paper study](professional/06_research_ownership.md) | Modules 9–10 | Reproducible handoff, independent challenge, prospective protocol and decision | Persistent records, replay, monitors and [committee template](templates/professional/committee_memo.md) |

Default research context is medium-horizon liquid-equity research because that matches the available workspace data. You can choose another market. Before expanding breadth, complete one coherent research chain deeply: mechanism → defensible observations → experiment → forecast → feasible positions → fills → attribution → decision. Low-latency market making, discretionary event research and slower systematic allocation need different specialties and engineering budgets.

## Run the new labs

From the apprenticeship directory:

```bash
python3 -m apprentice_system.frontier --output outputs/frontier
../QuantTimeLearn/.venv/bin/python -m apprentice_system.model_lab --output outputs/model_lab
../QuantTimeLearn/.venv/bin/python -m unittest discover -s tests -v
```

The first lab is standard-library, synthetic and offline. It demonstrates committed research choices, conditional date-block intervals, paired portfolio alternatives and an explicitly authored AI-evaluation fixture. The second actually trains zero/ridge/ablated-ridge/two small MLP procedures on local historical data, using the existing numerical environment. It depends on the sibling `BehaviorIRL` snapshots. Neither creates a new unseen sample or a profitable strategy.

[Synthetic research and economics report](outputs/frontier/frontier_report.json) · [Actual model comparison](outputs/model_lab/model_lab_report.json) · [Worked research decision](professional/WORKED_RESEARCH_DECISION.md).

## Architecture revision

```text
Market mechanism + competing beliefs + data diligence
                  ↓
Committed experiment protocol + trial/compute budget
                  ↓
Point-in-time data → frozen features → matched model comparisons
                  ↓
Ablations + falsification + locked selection + recorded evaluation exposure
                  ↓
Portfolio alternatives → risk → execution/capacity → horizon-aware attribution
                  ↓
Independent replication + incident exercise + committee decision
                  ↓
Prospective shadow study when authorized → measured decisions → research revision

AI assistance is evaluated throughout. Its outputs do not supply independent truth.
```

Trial locking prevents accidental in-API changes; it is not access control over evaluation files. A source or model timestamp is a declared provenance fact to verify, not proof of an uncontaminated model. A shared simulator makes policy comparisons more consistent but does not calibrate its market assumptions.

## How the standard of work changes

For each studio, submit the original decision, your implementation, one meaningful failure investigation, a comparison you could have lost, and the evidence that would reverse your conclusion. Prespecify the search budget and preserve failed attempts. A careful negative result can satisfy the research objective; an attractive unsupported result cannot.

Use [professional templates](templates/professional/research_agenda.md) and the existing five [learning records](FULL_PACKAGE.md#assessments-templates-and-learning-records). No proficiency level changes until actual learner evidence is reviewed. There is no requirement to obtain proprietary data, buy compute or use a paid LLM before working through the available material. Extensions requiring those resources remain proposals until their access and value are established.
