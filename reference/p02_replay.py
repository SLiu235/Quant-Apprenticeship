"""Synthetic FIFO queue. Prices in dollars, quantity in shares."""

from dataclasses import dataclass


@dataclass
class Passive:
    ahead: int
    remaining: int
    filled: int = 0
    cancelled: int = 0

    def trade(self, quantity):
        if quantity < 0:
            raise ValueError("negative trade")
        ahead_fill = min(quantity, self.ahead)
        self.ahead -= ahead_fill
        fill = min(quantity - ahead_fill, self.remaining)
        self.remaining -= fill
        self.filled += fill
        return fill

    def cancel(self):
        self.cancelled += self.remaining
        self.remaining = 0


def run():
    order = Passive(40, 40)
    tape = []
    for sequence, quantity in enumerate((25, 30), 1):
        fill = order.trade(quantity)
        tape.append(
            {
                "sequence": sequence,
                "trade_at_bid": quantity,
                "own_fill": fill,
                "ahead": order.ahead,
                "remaining": order.remaining,
            }
        )
    order.cancel()  # Acknowledged cancellation; request alone does not remove exposure.
    aggressive = order.cancelled
    notional = order.filled * 100.0 + aggressive * 100.04
    quantity, arrival = 40, 100.02
    fees = quantity * 0.004
    shortfall = notional + fees - quantity * arrival
    return {
        "data_kind": "synthetic, stipulated FIFO and sufficient ask",
        "tape": tape,
        "passive_filled": order.filled,
        "passive_cancelled": order.cancelled,
        "aggressive_filled": aggressive,
        "total_shares": quantity,
        "vwap": notional / quantity,
        "fee_dollars": fees,
        "shortfall_dollars": shortfall,
        "shortfall_bps": shortfall / (quantity * arrival) * 10000,
        "limitations": "No hidden liquidity, replenishment, cancel race or endogenous impact; not exchange fill model",
    }
