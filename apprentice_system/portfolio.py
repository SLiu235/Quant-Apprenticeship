"""Transparent allocation baseline: capped conviction, with residual cash."""
from math import floor
from .core import finite


def weights(alphas: dict[str, float], cap: float = 0.30, gross: float = 0.80,
            scale: float = 0.01) -> dict[str, float]:
    if not 0 < finite(cap, "cap") <= 1 or not 0 <= finite(gross, "gross") <= 1:
        raise ValueError("invalid long-only limits")
    if finite(scale, "scale") <= 0:
        raise ValueError("invalid conviction scale")
    raw = {s: min(cap, max(0.0, finite(a, "alpha")) / scale * cap) for s, a in alphas.items()}
    total = sum(raw.values())
    factor = min(1.0, gross / total) if total else 0.0
    return {s: value * factor for s, value in raw.items()}


def orders(target: dict[str, float], holdings: dict[str, int], equity: float,
           prices: dict[str, float], prefix: str) -> list[dict]:
    if finite(equity, "equity") <= 0:
        raise ValueError("nonpositive equity")
    if any(finite(w, "weight") < 0 for w in target.values()) or sum(target.values()) > 1 + 1e-12:
        raise ValueError("invalid target")
    output = []
    for symbol in sorted(set(target) | set(holdings)):
        price = finite(prices[symbol], "sizing price")
        if price <= 0 or type(holdings.get(symbol, 0)) is not int or holdings.get(symbol, 0) < 0:
            raise ValueError("invalid position or price")
        quantity = floor(target.get(symbol, 0) * equity / price) - holdings.get(symbol, 0)
        if quantity:
            output.append(dict(order_id=f"{prefix}:{symbol}", symbol=symbol,
                               quantity=quantity, decision_price=price))
    return sorted(output, key=lambda o: (o["quantity"] > 0, o["symbol"]))  # sells first
