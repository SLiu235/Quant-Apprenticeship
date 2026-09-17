# Lesson 11 answer key — Evaluate retrieval and research agents as systems

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Cost=1,000×(800×.20+100×.80)/1,000,000=$.24. Remaining inference budget=200−80−50−20=50 ms, before any omitted overhead; measure end-to-end tail latency rather than subtracting unrelated average timings. JSON validates shape; a substring validates presence, not attribution, completeness or financial relevance. Fixture a in Project 4 demonstrates this distinction.

## A2

Score at least four independent dimensions: eligible-relevant retrieval, schema/evidence validity, adjudicated interpretation and prohibited-action isolation. Include accepted coverage. A cached test is fully valid for checking evaluator behavior, but manually assigned outputs do not estimate a real model's quality. Each case needs gold evidence/label and expected failure category; the runner must surface every raw mismatch. A tool-instruction case passes only if no unauthorized tool action occurs, not merely if the final text says it refused.

Reference retrieval algorithm: filter `(available_at <= cutoff)` and entity/version eligibility; select latest eligible version per document; rank only that set; retain its IDs in the trace. A mock ranker is acceptable for software tests if clearly identified.

## A3

Freeze model/version, prompt, tokenizer, index policy and downstream decision mapping before collecting a fresh evaluation period. Log actual receipt and completion times, outages and abstentions; compare baseline and candidate on the declared population, with costs and full inference latency. Use a separate annotation sample to audit extraction. Refuse to call a 2026 model's predictions on 2025 events a historically deployable 2025 strategy without evidence about model training and availability. Date-masking a prompt does not remove memorized outcomes.

Repair: try a future-outcome document and an instruction hidden in a quoted post. Both must remain data, with future versions excluded before ranking.
