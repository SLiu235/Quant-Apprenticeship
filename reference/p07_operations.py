"""Synthetic paper state machine and measured CPU benchmark."""

from dataclasses import dataclass, field
import time, platform
import numpy as np


@dataclass
class PaperDesk:
    cash: float = 10000.0
    shares: int = 0
    halted: bool = False
    reconciled: bool = False
    fills: dict = field(default_factory=dict)
    orders: dict = field(default_factory=dict)

    def submit(self, oid, quantity, quote_age_ms):
        if self.halted:
            return "halted"
        if not np.isfinite(quote_age_ms) or quote_age_ms > 1000 or quote_age_ms < 0:
            self.halted = True
            return "stale_quote_halt"
        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or oid in self.orders
            or quantity <= 0
            or quantity > 50
            or self.shares + sum(self.orders.values()) + quantity > 100
        ):
            return "risk_reject"
        self.orders[oid] = quantity
        self.reconciled = False
        return "accepted"

    def fill(self, fid, oid, quantity, price):
        if fid in self.fills:
            if self.fills[fid] != (oid, quantity, price):
                self.halted = True
                self.reconciled = False
                return "conflicting_fill_halt"
            return "duplicate_ignored"
        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or oid not in self.orders
            or quantity <= 0
            or quantity > self.orders[oid]
            or price <= 0
            or not np.isfinite(price)
        ):
            self.halted = True
            self.reconciled = False
            return "invalid_fill_halt"
        self.orders[oid] -= quantity
        self.shares += quantity
        self.cash -= quantity * price
        self.fills[fid] = (oid, quantity, price)
        self.reconciled = False
        return "applied"  # Fills still reconcile while halted.

    def reconcile(self, broker_shares, broker_cash, broker_orders):
        self.reconciled = (
            broker_shares == self.shares
            and abs(broker_cash - self.cash) < 1e-8
            and broker_orders == self.orders
        )
        if not self.reconciled:
            self.halted = True
        return self.reconciled

    def resume(self, operator_approved, quote_age_ms):
        if (
            not operator_approved
            or not self.reconciled
            or not 0 <= quote_age_ms <= 1000
        ):
            return False
        self.halted = False
        return True


def run():
    rng = np.random.default_rng(42)
    x, w = rng.normal(size=(4000, 16)), rng.normal(size=16)
    slow = lambda: np.array(
        [sum(float(a) * float(b) for a, b in zip(row, w)) for row in x]
    )
    fast = lambda: x @ w
    a, b = slow(), fast()

    def timing(fn):
        durations = []
        for _ in range(7):
            start = time.perf_counter()
            fn()
            durations.append(time.perf_counter() - start)
        return {
            "median_seconds": float(np.median(durations)),
            "min_seconds": min(durations),
            "repetitions": 7,
        }

    desk = PaperDesk()
    events = [
        desk.submit("o1", 40, 100),
        desk.fill("f1", "o1", 15, 100.0),
        desk.fill("f1", "o1", 15, 100.0),
        desk.submit("o2", 10, 2000),
        desk.fill("f2", "o1", 25, 100.04),
        str(desk.resume(True, 100)),
    ]
    desk.reconcile(40, 5999.0, {"o1": 0})
    events.append(str(desk.resume(True, 100)))
    return {
        "data_kind": "synthetic operational events; real local CPU timing",
        "events": events,
        "cash": desk.cash,
        "shares": desk.shares,
        "halted": desk.halted,
        "equity_at_100_02": desk.cash + desk.shares * 100.02,
        "cpu": platform.processor() or platform.machine(),
        "numpy": np.__version__,
        "max_abs_difference": float(np.max(np.abs(a - b))),
        "loop": timing(slow),
        "vectorized": timing(fast),
        "limits": "No broker, persistent journal, sell handling or GPU measurement; timing is host/thread specific.",
    }
