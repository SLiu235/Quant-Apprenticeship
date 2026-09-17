"""Independent audit of saved predictions; no refit."""

from .common import recent_predictions, scores, date_deltas, block_interval, digest


def run():
    path, m = recent_predictions()
    dates, d = date_deltas(m["public"], m["market"])
    metrics = {k: scores(v["p"], v["y"]) for k, v in m.items()}
    return {
        "data_kind": "real saved predictions; inspected evaluation",
        "source_sha256": digest(path),
        "metrics": metrics,
        "primary": {
            "comparison": "public minus market NLL; negative favors public",
            "date_mean": float(d.mean()),
            "dates": len(dates),
            "date_range": [dates[0], dates[-1]],
            "ci95_by_block": {str(b): block_interval(d, b) for b in (1, 3, 5, 10)},
            "row_mean": metrics["public"]["nll"] - metrics["market"]["nll"],
        },
        "limits": [
            "Selected issuer-days, not Nasdaq population",
            "Assumed latency, missing receipt/edit clock",
            "Comment sampling depends on eventual engagement",
            "No participant IRL or tradable PnL",
        ],
    }
