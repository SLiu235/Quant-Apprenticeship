"""Limits, explicit scenarios and accounting attribution."""
from .core import finite


def check_weights(w: dict[str, float], cap: float = 0.30, gross: float = 0.80) -> None:
    if any(not 0 <= finite(x, "weight") <= cap + 1e-12 for x in w.values()):
        raise ValueError("concentration breach")
    if sum(w.values()) > gross + 1e-12:
        raise ValueError("gross exposure breach")


def scenarios(w: dict[str, float], shocks: dict[str, dict[str, float]]) -> dict:
    if any(set(w) - set(shock) for shock in shocks.values()):
        raise ValueError("scenario missing a held symbol")
    return {name: sum(finite(weight, "weight") * finite(shock[s], "shock") for s, weight in w.items())
            for name, shock in shocks.items()}


def attribution(old_holdings: dict, old_marks: dict, new_marks: dict, fills: list[dict]) -> dict:
    carry = {s: qty * (new_marks[s] - old_marks[s]) for s, qty in old_holdings.items()}
    trading, fees = {}, 0.0
    for fill in fills:
        s = fill["symbol"]
        trading[s] = trading.get(s, 0.0) + fill["quantity"] * (new_marks[s] - fill["price"])
        fees += fill["fee"]
    return {"carry_by_symbol": carry, "trade_to_mark_by_symbol": trading, "fees": fees,
            "net_pnl": sum(carry.values()) + sum(trading.values()) - fees}
