"""Expanding one-feature regression with frozen decision-time features."""
from math import sqrt
from statistics import mean
from .core import timestamp
from .data import asof, features


def fit(samples: list[tuple[float, float]]) -> dict:
    if len(samples) < 6:
        raise ValueError("insufficient training examples")
    mx, my = mean(x for x, _ in samples), mean(y for _, y in samples)
    denominator = sum((x - mx) ** 2 for x, _ in samples)
    slope = sum((x - mx) * (y - my) for x, y in samples) / max(denominator, 1e-12)
    intercept = my - slope * mx
    residual = sqrt(mean((y - intercept - slope * x) ** 2 for x, y in samples))
    return dict(intercept=intercept, slope=slope, residual_rmse=residual,
                training_rows=len(samples))


def walk_forward(dataset: dict) -> list[dict]:
    frozen, forecasts = [], []
    for day in dataset["days"]:
        cutoff = day + "T15:55:00+00:00"
        current = features(dataset["bars"], cutoff)
        labels = {(r["symbol"], r["event_at"][:10]): r
                  for r in asof(dataset["bars"], cutoff)}
        samples, releases = [], []
        for old in frozen:
            label = labels.get((old["symbol"], old["day"]))
            if label and timestamp(label["available_at"]) < timestamp(cutoff):
                samples.append((old["x"], label["close"] / label["mid"] - 1))
                releases.append(label["available_at"])
        if len(samples) >= 12:
            model = fit(samples)
            for symbol, f in sorted(current.items()):
                forecasts.append(dict(day=day, symbol=symbol, decision_at=cutoff,
                                      alpha=model["intercept"] + model["slope"] * f["x"],
                                      x=f["x"], sizing_price=f["price"],
                                      feature_available_at=f["available_at"],
                                      latest_training_label=max(releases), model=model))
        frozen.extend(dict(day=day, symbol=s, x=f["x"]) for s, f in sorted(current.items()))
    return forecasts


def evaluate(forecasts: list[dict], dataset: dict) -> dict:
    """Ex-post scoring is isolated from fitting. Fixture v1 labels are fixed."""
    labels = {(r["symbol"], r["event_at"][:10]): r for r in dataset["bars"] if r["version"] == 1}
    errors = {"linear": [], "zero": [], "persistence": []}
    for f in forecasts:
        r = labels[(f["symbol"], f["day"])]
        y = r["close"] / r["mid"] - 1
        for name, prediction in (("linear", f["alpha"]), ("zero", 0.0), ("persistence", f["x"])):
            errors[name].append((y - prediction) ** 2)
    if not forecasts:
        raise ValueError("no evaluation forecasts")
    return {"rows": len(forecasts), "mse": {k: mean(v) for k, v in errors.items()},
            "interpretation": "synthetic software evidence; dependent rows; no significance or alpha claim",
            "uncertainty": "residual RMSE is descriptive scale, not calibrated predictive confidence"}
