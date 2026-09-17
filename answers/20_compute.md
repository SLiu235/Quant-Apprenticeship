# Lesson 20 answer key — Spend compute on measured research bottlenecks

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Normalized runtime becomes.8+.2/10=.82; speedup 1/.82≈1.2195. Matrix memory 10^8×8=800 MB decimal≈762.94 MiB. A100× speedup in 1% of work gives 1/(.99+.0001)≈1.01 overall. Trading or research deadlines may be dominated by data receipt or sequential I/O instead.

## A2

The reference output records max numerical disagreement around 3.6e−15 on this host; do not hardcode an expected speedup. Warm both implementations, report median/min and repeat count, record Python/NumPy/CPU plus available BLAS/thread details, and state unmeasured settings. A meaningful benchmark changes input sizes and checks whether the benefit survives end-to-end work. GPU results are absent unless you actually ran a GPU path.

## A3

Laptop: independent audits, linear models, exact small MDPs and small NLP fixtures. Single GPU: controlled encoder inference/fine-tuning or sequence-model comparisons with frozen data/selection budget. Cluster: multi-seed/multi-regime simulation or large cross-asset feature processing with distributed correctness and cost accounting. None creates historical receipts, actor inventory, unbiased coverage or independent future market regimes. Cluster experiments also need shard boundaries and deterministic reduction/lineage policies.

Repair: if your budget lists hardware without specifying a decision it helps resolve, return to the experiment contract.
