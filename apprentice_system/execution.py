"""Signed quantities, partial IOC fills, spread and stipulated impact."""

from dataclasses import dataclass, field
from math import floor, sqrt
from .core import finite


@dataclass
class Ledger:
    cash: float = 100000.0
    holdings: dict[str, int] = field(default_factory=dict)
    fills: dict[str, dict] = field(default_factory=dict)

    def apply(self, fill: dict) -> bool:
        fid = fill["fill_id"]
        if fid in self.fills:
            if self.fills[fid] != fill:
                raise ValueError("conflicting duplicate fill")
            return False
        q, p, fee = (
            fill["quantity"],
            finite(fill["price"], "fill price"),
            finite(fill["fee"], "fee"),
        )
        if type(q) is not int or q == 0 or p <= 0 or fee < 0:
            raise ValueError("invalid fill")
        symbol = fill["symbol"]
        position, cash = self.holdings.get(symbol, 0) + q, self.cash - q * p - fee
        if position < 0 or cash < -1e-8:
            raise ValueError("short or cash limit breach")
        self.holdings[symbol], self.cash, self.fills[fid] = position, cash, dict(fill)
        return True

    def equity(self, marks: dict[str, float]) -> float:
        total = self.cash
        for symbol, qty in self.holdings.items():
            price = finite(marks[symbol], "mark")
            if price <= 0:
                raise ValueError("nonpositive mark")
            total += qty * price
        return total


def simulate(
    order: dict,
    quote: dict,
    participation: float = 0.05,
    impact_bps: float = 10.0,
    fee_per_share: float = 0.005,
) -> dict:
    q = order["quantity"]
    if type(q) is not int or q == 0 or order["symbol"] != quote["symbol"]:
        raise ValueError("invalid order")
    if not 0 < finite(participation, "participation") <= 1:
        raise ValueError("invalid participation")
    volume = quote["interval_volume"]
    if type(volume) is not int or volume < 0:
        raise ValueError("invalid interval volume")
    mid, spread = finite(quote["mid"], "mid"), finite(quote["spread_bps"], "spread")
    close = finite(quote["close"], "terminal benchmark")
    decision = finite(order["decision_price"], "decision benchmark")
    if close <= 0 or decision <= 0:
        raise ValueError("nonpositive benchmark")
    if (
        mid <= 0
        or spread < 0
        or finite(impact_bps, "impact") < 0
        or finite(fee_per_share, "fee") < 0
    ):
        raise ValueError("invalid execution assumptions")
    amount = min(abs(q), floor(volume * participation))
    direction = 1 if q > 0 else -1
    filled = direction * amount
    slippage = spread / 2 + impact_bps * sqrt(amount / volume) if volume else 0.0
    price = mid * (1 + direction * slippage / 10000)
    if price <= 0:
        raise ValueError("invalid impacted price")
    fill = (
        None
        if amount == 0
        else dict(
            fill_id=order["order_id"] + ":fill:1",
            order_id=order["order_id"],
            symbol=order["symbol"],
            quantity=filled,
            price=price,
            fee=amount * fee_per_share,
        )
    )
    return {
        "order": order,
        "fill": fill,
        "filled": filled,
        "cancelled": q - filled,
        "status": "filled" if filled == q else "IOC_remainder_cancelled",
        "arrival_shortfall_dollars": 0.0
        if fill is None
        else filled * (price - mid) + fill["fee"],
        "decision_shortfall_dollars": 0.0
        if fill is None
        else filled * (price - decision) + fill["fee"],
        "unfilled_opportunity_dollars": (q - filled) * (close - decision),
    }


def twap(quantity: int, slices: int) -> list[int]:
    if type(quantity) is not int or type(slices) is not int or slices <= 0:
        raise ValueError("integer quantity and positive slices required")
    base, remainder = divmod(abs(quantity), slices)
    sign = 1 if quantity >= 0 else -1
    return [sign * (base + (i < remainder)) for i in range(slices)]
