# Lesson 20 — Spend compute on measured research bottlenecks

Prerequisites: Lessons 13 and 19. Suggested effort: 5–7 hours, including the lab. Project: 7.

## Performance engineering starts with a complete workload

A faster matrix multiply matters only if it is a material part of the research path. Profile acquisition, parsing, feature construction, training, inference and reporting separately, then measure end-to-end time. Amdahl's law gives speedup 1/[(1−f)+f/s] if fraction f is sped up by s. If matrix work is 20% of runtime and becomes 10 times faster, total speedup is only 1/.82≈1.22.

Before accelerating, establish a CPU correctness reference. Compare outputs and downstream decisions within justified tolerances. Float 32, mixed precision and nondeterministic reductions can change borderline rankings or optimization. Tiny average numeric error may still flip a threshold decision, so report both numeric and decision disagreement.

Benchmark warm-up, repeated measurements, thread configuration, problem sizes and memory. Asynchronous GPU calls require synchronization around the measured workload; otherwise you may time launch overhead. Host-to-device transfers and batching can dominate small workloads. R18 explains measurement mechanics; optimized kernels do not excuse unmeasured end-to-end claims.

Our Project 7 compares a Python loop with NumPy matrix multiplication on the same local CPU inputs. It is a demonstration of vectorization, not a CPU-versus-GPU contest. It does not control every background process or library thread; report its host-specific measurement scope. A measured improvement here says nothing directly about an LLM service's tail latency.

## Worked resource choice

A10,000×10,000 float 64 dense matrix uses 800,000,000 bytes≈763 MiB for one array. Keeping input, covariance, gradients and copies can multiply this. If the task is a four-asset covariance calculation, moving to a GPU is unlikely to address the actual uncertainty. For a large text encoder, batching/caching can reduce repeated inference before buying faster hardware.

## Lab procedure

1. Run Project 7 three times and keep each timing record; compare medians and spread without selecting the fastest run.
2. Profile a complete Project 3 or text-processing run and estimate time fractions.
3. Validate a float 32 implementation against float 64 on both ordinary and near-threshold fixtures.
4. Write a resource budget with data size, memory, wall time and the research decision accelerated.
5. Optional GPU path: port only the measured bottleneck, warm up, synchronize, include transfer/end-to-end cost and record device/library versions. Lack of a GPU is not a course failure.

## Assignments

**A1.** Derive the Amdahl example and matrix memory. Explain why a 100× kernel speedup can be irrelevant to the desk.

**A2.** Submit a reproducible CPU benchmark with at least seven repeats after warm-up, correctness tolerance and end-to-end profile. Include all runs and host/thread settings you can observe.

**A3.** Prepare three resource plans: laptop, single GPU and larger cluster. For each, state one experiment newly feasible and one inference limitation unchanged.

Mastery check: every speedup claim has a workload, hardware, timing boundary and correctness comparison.

Check your work with the [answer key](../answers/20_compute.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
