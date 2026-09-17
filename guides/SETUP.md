# Setup and reproducible commands

The required course runs offline against files already in this Quant workspace. Python, NumPy and SciPy are sufficient. There is no required trading account, paid feed, API key, GPU or LLM subscription. Primary readings use the web; optional data/model extensions need their own access and provenance.

## Use the existing workspace runtime

Open a terminal and run these commands:

```bash
cd /Users/dexter/Desktop/Projects/Quant/AIQuantApprenticeship
../QuantTimeLearn/.venv/bin/python -m reference.run --project all
../QuantTimeLearn/.venv/bin/python -m unittest discover -s tests -v
```

Throughout the lessons, `python` means this interpreter or your own activated environment containing the dependencies. It does not mean that the system's default Python already has NumPy installed. Run one project with `--project 1` through `--project 8`.

To compare a fresh run while retaining the supplied output files:

```bash
../QuantTimeLearn/.venv/bin/python -m reference.run --project all --output submissions/reference_check
```

The verified runtime and source hashes are recorded in [verification.json](../outputs/verification.json). Core outputs are JSON; reference source code is ordinary Python, without hidden notebook state. CPU timing fields will vary. Solver results can vary slightly across numerical libraries; use the tolerances stated in the keys.

## Optional independent environment

Use Python 3.11 or newer with compatible NumPy/SciPy wheels. The course has been executed on the exact runtime recorded above; other environments require the same test suite.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m reference.run --project all
python -m unittest discover -s tests -v
```

Dependency installation needs internet access. It is unnecessary when using the existing runtime. Do not rename a local vendor snapshot or replace raw data just to force reference numbers to match.

## File dependencies

Projects 1/4/8 require `BehaviorIRL/results/reddit_recent_2026/predictions.csv`. Projects 3/5 require the four JSON price files under `BehaviorIRL/real_data/recent_prices/`. Project 6 imports the existing `BehaviorIRL/behavior_irl` planner and objective. Projects 2/7 use explicit synthetic fixtures. The supplemental solutions are self-contained aside from NumPy.

If moving the course, retain the sibling `BehaviorIRL` tree and use a compatible interpreter. The course resolves workspace paths from its source location, not your shell's current directory. The commands assume you launch modules from the course directory. The sources are left in their existing location to preserve provenance and avoid redistributing a second copy of social data.

## Troubleshooting

| Symptom | Diagnosis and repair |
|---|---|
| `No module named numpy` | Use the specified workspace interpreter or install the requirements into your activated environment. |
| `No module named reference` | Run from the course directory using `-m reference.run`. |
| Missing prediction/price file | Confirm the sibling workspace path; read the source audit before reacquiring anything. Do not replace missing real observations with simulations without relabeling the experiment. |
| Different score | Compare hashes, episode/class order, logarithm base and Brier convention before retraining. |
| Different bootstrap interval | Check sorted dates, within-date averaging, non-circular blocks, truncation, seed and RNG implementation. |
| Optimizer failure | Preserve failure details, check units/finite inputs/feasibility; do not accept the last iterate silently. |
| Different timing | Expected across runs; compare complete protocols and hardware rather than exact durations. |

Keep your work under `submissions/project_XX/`. Copy a reference before experimenting; preserve the saved source data and the original pilot. Read an answer key after your independent attempt, then solve a changed fixture to show understanding rather than memorization.
