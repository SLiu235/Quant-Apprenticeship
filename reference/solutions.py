"""Worked numerical solutions for lesson extensions.

These are small teaching components, not production market infrastructure.
All timestamps must have an explicit offset. No live service is called.
"""

from datetime import datetime
import json
import os
from pathlib import Path
import numpy as np


def instant(value):
    result = datetime.fromisoformat(value)
    if result.utcoffset() is None:
        raise ValueError("timezone required")
    return result


def asof_versions(rows, cutoff):
    cutoff = instant(cutoff)
    seen, selected = set(), {}
    for row in rows:
        key = (row["document_id"], row["version_id"])
        if key in seen:
            raise ValueError("duplicate version")
        seen.add(key)
        available = instant(row["available_at"])
        if available > cutoff:
            continue
        old = selected.get(row["document_id"])
        if old and available == instant(old["available_at"]):
            raise ValueError("ambiguous version time")
        if old is None or available > instant(old["available_at"]):
            selected[row["document_id"]] = dict(row)
    return [selected[k] for k in sorted(selected)]


def permitted_labels(rows, decision_at, evaluation_intervals=()):
    """Strict clock plus closed-interval outcome purge, as stipulated in Lesson9."""
    cutoff = instant(decision_at)
    intervals = [(instant(a), instant(b)) for a, b in evaluation_intervals]
    output = []
    for row in rows:
        start, end, available = map(
            instant, (row["start"], row["end"], row["available_at"])
        )
        if start > end or end > available:
            raise ValueError("invalid label interval")
        overlap = any(max(start, a) <= min(end, b) for a, b in intervals)
        if available <= cutoff and not overlap:
            output.append(row)
    return output


def edge_counts(rows, cutoff, coverage_known):
    """Explicit zero only under stipulated complete coverage; otherwise unknown."""
    if not coverage_known:
        return {"coverage": "unknown", "counts": None}
    now = instant(cutoff)
    counts = {}
    for row in rows:
        if instant(row["available_at"]) <= now:
            kind = row["type"]
            counts[kind] = counts.get(kind, 0) + 1
    return {"coverage": "observed", "counts": counts}


def importance_value(rewards, target, behavior, support_verified):
    rewards, target, behavior = map(
        lambda x: np.asarray(x, float), (rewards, target, behavior)
    )
    if not support_verified:
        return {"status": "unsupported", "value": None, "ess": None}
    if (
        rewards.ndim != 1
        or not len(rewards)
        or target.shape != rewards.shape
        or behavior.shape != rewards.shape
    ):
        raise ValueError("invalid shapes")
    if not all(np.isfinite(x).all() for x in (rewards, target, behavior)):
        raise ValueError("nonfinite input")
    if (
        (behavior <= 0).any()
        or (behavior > 1).any()
        or (target < 0).any()
        or (target > 1).any()
    ):
        raise ValueError("invalid probabilities")
    weights = target / behavior
    if weights.sum() == 0:
        return {"status": "no_target_mass_observed", "value": None, "ess": 0.0}
    return {
        "status": "conditional_on_support_assumption",
        "value": float(np.mean(weights * rewards)),
        "ess": float(weights.sum() ** 2 / (weights @ weights)),
    }


def mlp_loss_grad(parameters, x, y):
    w1, b1, w2, b2 = parameters
    h = np.tanh(x @ w1 + b1)
    prediction = h @ w2 + b2
    error = prediction - y
    e = 2 * error / len(y)
    hidden = (e[:, None] * w2[None, :]) * (1 - h * h)
    gradient = [x.T @ hidden, hidden.sum(0), h.T @ e, np.array(e.sum())]
    return float(np.mean(error**2)), gradient


def mlp_fit(
    x, y, validation_x, validation_y, width=4, epochs=200, seed=42, learning_rate=0.02
):
    """Fixed-budget full-batch MLP; validation-only checkpoint selection."""
    rng = np.random.default_rng(seed)
    mu, sd = x.mean(0), np.maximum(x.std(0), 1e-8)
    x = (x - mu) / sd
    vx = (validation_x - mu) / sd
    parameters = [
        rng.normal(0, 0.1, (x.shape[1], width)),
        np.zeros(width),
        rng.normal(0, 0.1, width),
        np.array(0.0),
    ]
    best_loss = np.inf
    best = None
    best_epoch = None
    for epoch in range(epochs):
        _, grad = mlp_loss_grad(parameters, x, y)
        parameters = [p - learning_rate * g for p, g in zip(parameters, grad)]
        val, _ = mlp_loss_grad(parameters, vx, validation_y)
        if val < best_loss:
            best_loss = val
            best = [p.copy() for p in parameters]
            best_epoch = epoch + 1
    return {
        "mu": mu,
        "sd": sd,
        "parameters": best,
        "validation_mse": best_loss,
        "chosen_epoch": best_epoch,
    }


def mlp_predict(model, x):
    w1, b1, w2, b2 = model["parameters"]
    return np.tanh((x - model["mu"]) / model["sd"] @ w1 + b1) @ w2 + b2


def gradient_error():
    rng = np.random.default_rng(42)
    x = rng.normal(size=(7, 3))
    y = rng.normal(size=7)
    p = [
        rng.normal(size=(3, 4)) * 0.1,
        np.zeros(4),
        rng.normal(size=4) * 0.1,
        np.array(0.0),
    ]
    _, gradient = mlp_loss_grad(p, x, y)
    error = 0.0
    eps = 1e-6
    for index, array in enumerate(p):
        for loc in np.ndindex(array.shape):
            plus = [a.copy() for a in p]
            minus = [a.copy() for a in p]
            plus[index][loc] += eps
            minus[index][loc] -= eps
            finite = (mlp_loss_grad(plus, x, y)[0] - mlp_loss_grad(minus, x, y)[0]) / (
                2 * eps
            )
            error = max(error, abs(float(finite - gradient[index][loc])))
    return error


def journal_append(path, event):
    """Single-writer JSONL write-ahead teaching journal. No live execution side effects.

    Fsync before the caller applies the event. Replay from genesis deduplicates exact
    IDs. A crash leaving a partial final line is detected and requires explicit repair;
    we do not silently discard unknown financial events or claim atomic network writes.
    """
    payload = json.dumps(event, sort_keys=True, allow_nan=False) + "\n"
    with Path(path).open("a") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())


def journal_replay(path, apply):
    seen = {}
    for line in Path(path).read_text().splitlines():
        event = json.loads(line)  # Corrupt/partial lines fail closed.
        key = event["id"]
        if key in seen:
            if seen[key] != event:
                raise ValueError("conflicting repeated event ID")
            continue
        apply(event)
        seen[key] = event
    return len(seen)
