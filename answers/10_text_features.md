# Lesson 10 answer key — Define the NLP task before selecting a language model

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Five fixtures are eligible: a,b,c,d,f. e is after the cutoff and excluded, even though its label is easy. Four pass the reference's label/evidence check: a,b,c,d. Three are valid nonabstentions: a,b,c. Coverage 3/5=.6; accepted accuracy 2/3. Fixture a is semantically wrong despite an exact quote; f fails because its claimed quote is absent; d abstains from the embedded trading instruction. These tiny counts demonstrate evaluation mechanics, not expected model quality.

## A2

A complete guide states entity/aspect, factual versus quoted voice, horizon, negation handling and ambiguity policy. Accept multiple justified labels for genuinely ambiguous examples only if the evaluation policy accounts for them in advance. Your lexical baseline will likely fail sarcasm and mixed statements; those failures earn credit if documented. The confusion matrix uses gold rows/predicted columns with a stated label order. Report rejected and abstained cases alongside accepted accuracy, not as quietly deleted rows.

For market evaluation, keep the same eligible episodes across candidate and baseline; use a defined missing/abstain feature or compare on a prespecified common population with its changed estimand disclosed. Do not give each model a different favorable subset.

## A3

Freeze the encoder/version and all text processing before independent evaluation. Fit downstream parameters on training dates, choose hyperparameters on validation, group copied/near-duplicate events, and freeze entity mapping rules. R9 supports a sentiment model, not a return predictor. A newly trained encoder may also know future historical events; Lesson 11 handles that contamination. Repair by separating annotation evaluation from market-outcome evaluation in your report.
