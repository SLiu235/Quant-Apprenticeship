"""Actionable alerts on clocks, reconciliation and observed exposures."""
from .core import finite, timestamp


def alerts(now: str, quote_at: str, equity: float, expected_equity: float,
           gross_weight: float, largest_weight: float, max_age: float = 60) -> list[str]:
    age = (timestamp(now) - timestamp(quote_at)).total_seconds()
    values = (equity, expected_equity, gross_weight, largest_weight, max_age)
    try:
        for value in values:
            finite(value, "monitor input")
    except ValueError:
        return ["invalid_numeric_state"]
    result = []
    if age < 0 or age > max_age:
        result.append("invalid_or_stale_quote")
    if abs(equity - expected_equity) > 1e-7:
        result.append("pnl_reconciliation_failure")
    if equity <= 0:
        result.append("nonpositive_equity")
    if gross_weight > 0.85 or largest_weight > 0.35:
        result.append("post_fill_exposure_breach")
    return result
