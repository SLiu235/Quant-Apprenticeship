"""Rolling intraday risk and constrained minimum-variance portfolios."""

import numpy as np
from scipy.optimize import minimize
from .common import price_panel


def covariance(r, shrink=0.5):
    s = np.cov(r, rowvar=False, ddof=1)
    return (1 - shrink) * s + shrink * np.diag(np.diag(s)) + np.eye(s.shape[0]) * 1e-10


def allocate(s):
    n = len(s)
    scale = max(np.trace(s) / n, 1e-12)
    opt = minimize(
        lambda w: (float(w @ s @ w / scale), 2 * s @ w / scale),
        np.ones(n) / n,
        jac=True,
        method="SLSQP",
        bounds=[(0.0, 0.5)] * n,
        constraints=[
            {"type": "eq", "fun": lambda w: w.sum() - 1, "jac": lambda w: np.ones(n)}
        ],
        options={"ftol": 1e-12, "maxiter": 200},
    )
    if (
        not opt.success
        or abs(opt.x.sum() - 1) > 1e-8
        or (opt.x < -1e-8).any()
        or (opt.x > 0.50000001).any()
    ):
        raise RuntimeError(str(opt.message))
    return opt.x


def run():
    days, r, _ = price_panel()
    realized = []
    forecast = []
    baseline = []
    ewma_forecasts = []
    gross = []
    equal = []
    risks = []
    ewma = (r[:60] ** 2).mean(0)
    for t in range(60, len(r)):
        if t > 60:
            ewma = 0.94 * ewma + 0.06 * r[t - 1] ** 2
        ewma_forecasts.append(np.maximum(ewma, 1e-10).copy())
        window = r[t - 60 : t]
        variance = np.maximum((window[-20:] ** 2).mean(0), 1e-10)
        persistence = np.maximum(r[t - 1] ** 2, 1e-10)
        s = covariance(window)
        w = allocate(s)
        realized.append(r[t] ** 2)
        forecast.append(variance)
        baseline.append(persistence)
        gross.append(w @ r[t])
        equal.append(r[t].mean())
        risks.append(w @ s @ w)
    realized, forecast, baseline = map(np.array, (realized, forecast, baseline))
    qlike = lambda f: float(np.mean(np.log(f) + realized / f))
    return {
        "data_kind": "real intraday returns; retrospective selected universe",
        "dates": len(gross),
        "range": [days[60], days[-1]],
        "qlike_rolling20": qlike(forecast),
        "qlike_previous_squared": qlike(baseline),
        "qlike_ewma94": qlike(np.array(ewma_forecasts)),
        "realized_to_forecast_second_moment": float(realized.sum() / forecast.sum()),
        "mean_gross_minvar_bps": float(np.mean(gross) * 10000),
        "mean_gross_equal_bps": float(np.mean(equal) * 10000),
        "minvar_realized_std_bps": float(np.std(gross, ddof=1) * 10000),
        "equal_realized_std_bps": float(np.std(equal, ddof=1) * 10000),
        "mean_predicted_portfolio_variance": float(np.mean(risks)),
        "last_weights": w.tolist(),
        "last_covariance_condition": float(np.linalg.cond(s)),
        "net_mean_at_5bps_one_way": float((np.mean(gross) - 0.001) * 10000),
        "limits": "QLIKE targets second moments with mean-zero approximation; centered portfolio covariance. Flat-to-flat turnover=2; no impact model.",
    }
