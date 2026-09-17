"""Inspectible local-only tools; no trading connections."""

from pathlib import Path
import csv, hashlib, json
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo

COURSE = Path(__file__).resolve().parents[1]
WORKSPACE = COURSE.parent
DATA = WORKSPACE / "BehaviorIRL"
ET = ZoneInfo("America/New_York")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scores(p, y):
    p, y = np.asarray(p, float), np.asarray(y, int)
    if p.ndim != 2 or len(p) != len(y) or not len(y):
        raise ValueError("invalid shape")
    if not np.isfinite(p).all() or (p < 0).any() or not np.allclose(p.sum(1), 1):
        raise ValueError("invalid probabilities")
    if (y < 0).any() or (y >= p.shape[1]).any():
        raise ValueError("invalid class")
    return {
        "nll": float(-np.log(np.maximum(p[np.arange(len(y)), y], 1e-15)).mean()),
        "brier": float(((p - np.eye(p.shape[1])[y]) ** 2).sum(1).mean()),
        "accuracy": float((p.argmax(1) == y).mean()),
        "rows": len(y),
    }


def recent_predictions():
    path = DATA / "results/reddit_recent_2026/predictions.csv"
    with path.open() as f:
        rows = list(csv.DictReader(f))
    models = {}
    for name in sorted({r["model"] for r in rows}):
        g = sorted([r for r in rows if r["model"] == name], key=lambda r: r["episode"])
        if len({r["episode"] for r in g}) != len(g):
            raise ValueError("duplicate episode")
        models[name] = {
            "ids": [r["episode"] for r in g],
            "dates": [r["trade_date"] for r in g],
            "y": np.array([int(r["target"]) for r in g]),
            "p": np.array(
                [
                    [
                        float(r[c])
                        for c in (
                            "p_negative_response",
                            "p_neutral",
                            "p_positive_response",
                        )
                    ]
                    for r in g
                ]
            ),
        }
    anchor = models["market"]
    for m in models.values():
        if (
            m["ids"] != anchor["ids"]
            or m["dates"] != anchor["dates"]
            or not np.array_equal(m["y"], anchor["y"])
        ):
            raise ValueError("unpaired models")
    return path, models


def date_deltas(a, b):
    loss = -np.log(a["p"][np.arange(len(a["y"])), a["y"]]) + np.log(
        b["p"][np.arange(len(b["y"])), b["y"]]
    )
    dates = sorted(set(a["dates"]))
    return dates, np.array([loss[np.array(a["dates"]) == d].mean() for d in dates])


def block_interval(values, block=3, repeats=1000, seed=42):
    """Non-circular moving blocks, equal date weights; exploratory conditional CI."""
    values = np.asarray(values, float)
    if not 1 <= block <= len(values):
        raise ValueError("invalid block")
    rng = np.random.default_rng(seed)
    means = []
    for _ in range(repeats):
        starts = rng.integers(
            0, len(values) - block + 1, size=int(np.ceil(len(values) / block))
        )
        sample = np.concatenate([values[s : s + block] for s in starts])[: len(values)]
        means.append(sample.mean())
    return np.quantile(means, [0.025, 0.975]).tolist()


def price_panel():
    """Close/open intraday returns; fixed retrospectively selected universe."""
    series, sources = {}, {}
    for ticker in ("ASML", "MU", "SNDK", "WDC"):
        path = DATA / f"real_data/recent_prices/{ticker}.json"
        raw = json.loads(path.read_text())["chart"]["result"][0]
        q = raw["indicators"]["quote"][0]
        series[ticker] = {}
        for stamp, op, cl in zip(raw["timestamp"], q["open"], q["close"]):
            if op is None or cl is None or op <= 0 or cl <= 0:
                continue
            series[ticker][datetime.fromtimestamp(stamp, ET).date().isoformat()] = (
                cl / op - 1
            )
        sources[ticker] = {
            "path": str(path.relative_to(WORKSPACE)),
            "sha256": digest(path),
        }
    days = sorted(set.intersection(*(set(s) for s in series.values())))
    if len(days) < 150:
        raise ValueError("insufficient common dates")
    returns = np.array([[series[t][d] for t in series] for d in days])
    if not np.isfinite(returns).all():
        raise ValueError("nonfinite returns")
    return days, returns, sources
