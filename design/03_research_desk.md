# Design round 3 — a complete self-paced research-desk apprenticeship

**Editorial simulation.** The executive review is an invented critical role. No real CEO or firm participated, and it is not an independent external certification.

## Final design reviewed

Twenty-four written lessons form eight integrated projects. Every lesson has teaching, a worked example, a lab procedure, three assignments and a matching answer key. Eight executable core examples have saved results. Additional numerical solutions cover version-aware joins, interval purging, graph coverage, importance sampling, MLP gradients/checkpoints and durable-journal replay. The course supplies primary readings, setup, source/compute choices, templates, grading, remediation and a capstone defense.

The sequence begins with an unfavorable real-data result and ends with a research decision. Modern AI appears where it changes the workflow: extraction, temporal retrieval, model-date contamination, agent evaluation, deep-model selection and measured inference. Extended sessions change calendar, data and operations requirements; they do not justify relabeling daytime observations.

## Simulated CEO critique of the implemented package

“This is much closer to what I would expect a junior researcher to own. I still see ways a student could pass by comparing against a weak control, or mistake a clean toy result for deployable evidence. Make those weaknesses visible in the worked projects themselves. The answers must teach when to stop, and the launch instructions must work without waiting for you.”

Concrete findings and revisions:

| Finding | Change made | Evidence |
|---|---|---|
| Risk example could look strong only because yesterday's squared return is a fragile baseline | Added a fixed-decay EWMA comparator to the runnable reference and explained why the small rolling/EWMA difference needs paired uncertainty | `reference/p05_risk.py`, output and Lesson 14 key |
| IRL reference had favorable known dynamics, with too little direct baseline comparison | Added training-frequency, behavior-cloning and training-estimated-dynamics IRL scores on the same 481 active test decisions | `reference/p06_irl.py`, output and Project 6 |
| A repeated fill ID with a different payload might silently disappear | Added conflicting-ID halt and nonfinite-quote rejection, preserving financial state | Project 7 code and fault tests |
| Small synthetic NLP cases might be mistaken for a real model benchmark | Explicit synthetic/cached labels in code, outputs, lessons and project; live model evaluation remains a separately recorded optional extension | Project 4 and Lessons 10–11 |
| Self-paced instructions must provide recovery when answers differ | Added diagnostic, numerical tolerances, symptom-based troubleshooting, graded repair and changed-fixture retests | Setup, answer keys and mastery guide |
| Broad “professional mastery” language can obscure specialization gaps | Defined demonstrated core competencies and post-course specialist projects; no employment, alpha or all-market mastery guarantee | Mastery and data/compute guides |

## Executive decision and remaining boundaries

Release the package for self-paced core training after its commands, links and numerical checks pass. Do not call the course an empirical validation of current social sentiment, participant IRL, causal propagation or 23-hour execution. The social source ends in early 2026; newer local price bars do not extend it. Internal execution logs, licensed feeds and GPU/API experiments are optional access-dependent work, with explicit acceptance criteria.

The student must extend the worked cores, not simply rerun them for credit. Open-ended assignments are graded on complete evidence and interpretation rather than matching a favorable outcome. External review remains valuable; this simulated critique cannot substitute for an independent capstone reviewer.

Rejected request: require a profitable capstone or mandatory premium model subscription. Both would reward resources/noise rather than research judgment. The release audit records actual executed evidence separately from this editorial decision.
