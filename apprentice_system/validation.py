"""Dependence-aware descriptive intervals and chronological label eligibility."""

from datetime import timedelta
import random
from statistics import mean
from .core import finite, timestamp


def eligible_training(
    rows: list[dict], decision_at: str, gap_seconds: float = 0
) -> list[dict]:
    """Past-only split. Gap is before test; it is NOT post-test CV embargo."""
    if finite(gap_seconds, "gap") < 0:
        raise ValueError("negative gap")
    boundary = timestamp(decision_at) - timedelta(seconds=gap_seconds)
    output = []
    for row in rows:
        start, end = timestamp(row["label_start"]), timestamp(row["label_end"])
        available = timestamp(row["label_available_at"])
        feature = timestamp(row["feature_available_at"])
        if end < start or available < end or feature > start:
            raise ValueError("invalid sample timeline")
        if end < boundary and available < boundary:
            output.append(row)
    return output


def paired_date_interval(
    candidate: list[dict],
    baseline: list[dict],
    block: int = 3,
    repeats: int = 1000,
    seed: int = 7,
) -> dict:
    """Equal weight per date, noncircular moving-block percentile interval.

    Inputs contain id, date, loss. Candidate-minus-baseline < 0 favors candidate.
    This is conditional on a specified candidate, not a search-adjusted test.
    """

    def index(rows):
        result = {}
        for row in rows:
            key = row["id"]
            if key in result:
                raise ValueError("duplicate sample ID")
            result[key] = (row["date"], finite(row["loss"], "loss"))
        return result

    a, b = index(candidate), index(baseline)
    if not a or set(a) != set(b) or any(a[k][0] != b[k][0] for k in a):
        raise ValueError("unmatched comparison populations")
    by_date = {}
    for key in sorted(a):
        by_date.setdefault(a[key][0], []).append(a[key][1] - b[key][1])
    values = [mean(by_date[d]) for d in sorted(by_date)]
    n = len(values)
    if (
        type(block) is not int
        or not 1 <= block <= n
        or type(repeats) is not int
        or repeats < 100
    ):
        raise ValueError("invalid bootstrap settings")
    rng = random.Random(seed)
    means = []
    for _ in range(repeats):
        sample = []
        while len(sample) < n:
            start = rng.randrange(n - block + 1)
            sample.extend(values[start : start + block])
        means.append(mean(sample[:n]))
    means.sort()

    def quantile(p):
        pos = (len(means) - 1) * p
        lower = int(pos)
        upper = min(lower + 1, len(means) - 1)
        return means[lower] + (means[upper] - means[lower]) * (pos - lower)

    return dict(
        mean_delta=mean(values),
        interval_95=[quantile(0.025), quantile(0.975)],
        dates=n,
        observations=len(a),
        block=block,
        repeats=repeats,
        scope="conditional descriptive interval; no multiple-search correction; stationarity/dependence assumptions require review",
    )
