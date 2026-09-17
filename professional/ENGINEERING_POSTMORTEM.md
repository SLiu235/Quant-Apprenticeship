# Reference-code postmortem — author review, not learner work

## Symptom

The simulator claimed quote-freshness checks, but the check received the same timestamp for current time and quote time. It could not detect either stale or future execution quotes. Duplicate quotes were collapsed into a dictionary without a uniqueness check. Nonfinite terminal benchmarks could contaminate opportunity-cost output.

## Root cause

The fixture supplied valid, unique observations and the integration code reused fixture metadata as the independent clock. The tests checked the monitor in isolation but did not challenge how the replay supplied its inputs. Benchmark validation was incomplete at the execution interface.

## Why it escaped detection

Most prior tests verified plausible inputs and component-level arithmetic. A correct monitor does not help when the caller passes self-confirming arguments. The integration suite lacked a future-quote mutation and duplicate-snapshot fixture.

## Fix

Compare quote timestamps with the replay's scheduled execution clock; validate the snapshot even for a cash policy; reject duplicate quotes and missing/duplicate forecast symbols; validate terminal and decision prices before execution arithmetic.

The replay also keeps the previous accounting mark separately from the research sizing price. A revised research price can change order sizing but cannot retroactively rewrite starting NAV. A changed-sizing-price fixture verifies that accumulated daily attribution still equals the final change in equity.

## Regression tests

The new tests inject a future quote into a no-order session, duplicate a quote, duplicate a forecast, and supply a NaN terminal benchmark. Separate tests reconcile the added overnight/intraday/cost attribution with ledger P&L and verify cash/equal-weight baselines.

## Monitoring improvement

Clock ownership is explicit at the caller boundary. Subsequent real-data work must also verify source sequencing, receipt latency and missing/stale feature behavior, not only execution quote age. Reference monitors are still limited local checks.

## Lesson

Test the information an interface supplies, not just the function receiving it. A safety check can be logically correct and operationally useless if its inputs cannot contradict each other.
