"""Chronological ridge on local recent bars. All evaluation dates are teaching data."""

import numpy as np
from .common import price_panel


def design(r):
    x = np.array(
        [
            np.column_stack([r[t - 1], r[t - 5 : t].mean(0), r[t - 20 : t].std(0)])
            for t in range(20, len(r))
        ]
    )
    return x, r[20:]


def fit(x, y, penalty):
    x, y = x.reshape(-1, x.shape[-1]), y.ravel()
    mu, sd = x.mean(0), np.maximum(x.std(0), 1e-8)
    z = np.column_stack([np.ones(len(x)), (x - mu) / sd])
    reg = np.diag([0.0, penalty, penalty, penalty])
    w = np.linalg.solve(z.T @ z / len(z) + reg, z.T @ y / len(z))
    return mu, sd, w


def predict(model, x):
    mu, sd, w = model
    shape = x.shape[:-1]
    z = np.column_stack(
        [np.ones(np.prod(shape, dtype=int)), ((x - mu) / sd).reshape(-1, x.shape[-1])]
    )
    return (z @ w).reshape(shape)


def run():
    days, r, sources = price_panel()
    x, y = design(r)
    days = days[20:]
    train, test = int(len(days) * 0.6), int(len(days) * 0.8)
    candidates = (0.01, 0.1, 1.0)
    val = {
        p: float(
            np.mean(
                (predict(fit(x[:train], y[:train], p), x[train:test]) - y[train:test])
                ** 2
            )
        )
        for p in candidates
    }
    chosen = min(val, key=val.get)
    predictions = []
    refits = []
    for t in range(test, len(days)):
        if (t - test) % 20 == 0:
            model = fit(x[:t], y[:t], chosen)
            refits.append(
                {
                    "decision_date": days[t],
                    "last_label_date": days[t - 1],
                    "training_dates": t,
                }
            )
        predictions.append(predict(model, x[t : t + 1])[0])
    pred = np.array(predictions)
    weights = np.sign(pred) / y.shape[1]
    gross = np.sum(weights * y[test:], axis=1)
    turnover = 2 * np.abs(weights).sum(1)  # Flat at each open and after each close.
    return {
        "data_kind": "real bars; selected four issuers; inspected teaching evaluation",
        "sources": sources,
        "common_dates": len(r),
        "test_dates": len(gross),
        "test_range": [days[test], days[-1]],
        "chosen_penalty": chosen,
        "validation_mse": {str(k): v for k, v in val.items()},
        "refits": refits,
        "mse_model": float(np.mean((pred - y[test:]) ** 2)),
        "mse_zero": float(np.mean(y[test:] ** 2)),
        "mean_gross_bps_per_day": float(gross.mean() * 10000),
        "mean_net_bps_by_one_way_cost": {
            str(c): float((gross - turnover * c / 10000).mean() * 10000)
            for c in (0, 5, 10, 25)
        },
        "mean_turnover": float(turnover.mean()),
        "break_even_one_way_bps": float(gross.mean() / turnover.mean() * 10000),
        "execution_status": "Open/close marks assumed; no guaranteed fills, borrow, impact or financing; not executable performance",
    }
