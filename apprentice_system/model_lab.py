"""Real local-data comparison: zero, ridge, ablation, and trained small MLPs.

Requires the existing NumPy environment and sibling BehaviorIRL price snapshots.
All dates are INSPECTED DEVELOPMENT data. No prospective performance is claimed.
"""

import argparse
from hashlib import sha256
from pathlib import Path
import platform
import time
import numpy as np
from .core import encoded, fingerprint, source_hashes
from .research_control import ExperimentBook
from .validation import paired_date_interval
from reference.common import price_panel
from reference.p03_baseline import design, fit, predict
from reference.solutions import mlp_fit, mlp_predict


def compare_models(
    x: np.ndarray, y: np.ndarray, days: list[str], sources: dict, output: Path
) -> dict:
    if x.ndim != 3 or y.shape != x.shape[:2] or len(days) != len(y) or len(days) < 30:
        raise ValueError("invalid panel or insufficient dates")
    if (
        len(set(days)) != len(days)
        or days != sorted(days)
        or not np.isfinite(x).all()
        or not np.isfinite(y).all()
    ):
        raise ValueError("invalid dates or values")
    output.mkdir(parents=True, exist_ok=True)
    a, b = int(len(days) * 0.6), int(len(days) * 0.8)
    protocol = dict(
        hypothesis="Nonlinearity or lag detail improves a frozen price-feature baseline",
        primary_metric="MSE with equal date weights",
        universe="fixed retrospectively selected four-issuer panel",
        horizon="open-to-close decimal return",
        data_hash=fingerprint(sources),
        split=dict(
            train_end=days[a - 1], validation_end=days[b - 1], evaluation_start=days[b]
        ),
        cost_policy="forecast-only comparison; portfolio economics evaluated separately",
        kill_rule="do not prefer complexity without robust incremental evidence",
        evaluation_status="inspected_development",
        seed=42,
        epochs=200,
        python=platform.python_version(),
        numpy=np.__version__,
        feature_bytes_sha256=sha256(np.ascontiguousarray(x).tobytes()).hexdigest(),
        target_bytes_sha256=sha256(np.ascontiguousarray(y).tobytes()).hexdigest(),
        input_schema=dict(
            x_shape=list(x.shape),
            y_shape=list(y.shape),
            x_dtype=str(x.dtype),
            y_dtype=str(y.dtype),
        ),
        source_hash=fingerprint(source_hashes()),
        reference_hashes={
            name: sha256(
                (Path(__file__).parents[1] / "reference" / name).read_bytes()
            ).hexdigest()
            for name in ("p03_baseline.py", "solutions.py", "common.py")
        },
    )
    study_id = fingerprint(protocol)
    book = ExperimentBook(output / "experiments.sqlite")
    models, scores, timings, descriptions = {}, {}, {}, {}
    tx, vx, ex = (v.reshape(-1, x.shape[-1]) for v in (x[:a], x[a:b], x[b:]))
    ty, vy = y[:a].ravel(), y[a:b].ravel()
    # Fit target scaling only on training data; features are scaled inside models.
    scale = max(float(ty.std()), 1e-8)
    names = ("zero", "ridge", "ridge_without_lag1", "mlp4", "mlp8")
    try:
        book.register(study_id, protocol, budget=len(names))
        for name in names:
            width = 4 if name == "mlp4" else 8
            spec = dict(
                name=name,
                seed=42,
                ridge_penalty=1.0,
                epochs=200 if name.startswith("mlp") else 0,
                checkpoint_policy="validation-only best epoch"
                if name.startswith("mlp")
                else "no checkpoint search",
            )
            book.reserve(study_id, name, spec)
            start = time.perf_counter()
            if name == "zero":
                model, val = None, np.zeros_like(vy)
                description = {"family": "zero"}
            elif name.startswith("ridge"):
                train, valid = x[:a].copy(), x[a:b].copy()
                if name == "ridge_without_lag1":
                    train[..., 0] = valid[..., 0] = 0
                model = fit(train, y[:a], 1.0)
                val = predict(model, valid).ravel()
                description = {
                    "family": name,
                    "parameters": [v.tolist() for v in model],
                }
            else:
                model = mlp_fit(
                    tx, ty / scale, vx, vy / scale, width=width, epochs=200, seed=42
                )
                val = mlp_predict(model, vx) * scale
                description = {
                    "family": name,
                    "chosen_epoch": model["chosen_epoch"],
                    "target_scale": scale,
                    "mu": model["mu"].tolist(),
                    "sd": model["sd"].tolist(),
                    "parameters": [p.tolist() for p in model["parameters"]],
                }
            if not np.isfinite(val).all():
                book.finish(
                    study_id, name, dict(status="failed", reason="nonfinite validation")
                )
                raise ValueError("model produced nonfinite outputs")
            timings[name] = time.perf_counter() - start
            scores[name] = float(np.mean((val - vy) ** 2))
            models[name], descriptions[name] = model, description
            book.finish(
                study_id,
                name,
                dict(
                    status="completed",
                    validation_mse=scores[name],
                    model_hash=fingerprint(description),
                ),
            )
        selected = min(scores, key=lambda n: (scores[n], n))
        book.lock_selection(study_id, selected)
        losses, output_predictions = {}, {}
        for name in names:
            if name == "zero":
                pred = np.zeros_like(y[b:])
            elif name.startswith("ridge"):
                test_x = x[b:].copy()
                if name == "ridge_without_lag1":
                    test_x[..., 0] = 0
                pred = predict(models[name], test_x)
            else:
                pred = (mlp_predict(models[name], ex) * scale).reshape(y[b:].shape)
            losses[name] = [
                dict(id=f"{d}:{j}", date=d, loss=float((pred[i, j] - y[b + i, j]) ** 2))
                for i, d in enumerate(days[b:])
                for j in range(y.shape[1])
            ]
            output_predictions[name] = pred.tolist()
        comparison = paired_date_interval(
            losses[selected], losses["zero"], block=min(5, len(days) - b)
        )
        evaluation = dict(
            selected_before_exposure=selected,
            mse={
                name: float(np.mean([r["loss"] for r in rows]))
                for name, rows in losses.items()
            },
            primary_selected_vs_zero=comparison,
            secondary="all-model/ablation results are descriptive, not new selection evidence for an unseen claim",
        )
        book.record_evaluation(study_id, evaluation)
        result = dict(
            study=book.snapshot(study_id),
            models=descriptions,
            predictions=output_predictions,
            evaluation_dates=days[b:],
            evaluation=evaluation,
            measured_fit_seconds=timings,
            sources=sources,
            data_status="real snapshots; inspected development; no historical feed-receipt proof",
            limits="selected four-issuer universe; no independent prospective sample; pooled MSE; no executed trades; single fixed seed per MLP; checkpoint selection counted within declared 200-epoch procedure",
        )
        (output / "model_lab_report.json").write_bytes(encoded(result))
        return result
    finally:
        book.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("outputs/model_lab"))
    args = parser.parse_args()
    days, returns, sources = price_panel()
    x, y = design(returns)
    report = compare_models(x, y, days[20:], sources, args.output)
    print(
        f"Real-data development comparison complete. Selected procedure: {report['evaluation']['selected_before_exposure']}. No unseen or trading-performance claim."
    )


if __name__ == "__main__":
    main()
