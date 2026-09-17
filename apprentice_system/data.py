"""Versioned synthetic bars and point-in-time selection; stdlib only."""
from datetime import date, timedelta
import random
from .core import finite, timestamp

SYMBOLS = ("AAA", "BBB", "CCC")


def fixture(seed: int = 7, sessions: int = 60) -> dict:
    if sessions < 15:
        raise ValueError("at least 15 sessions required")
    rng = random.Random(seed)
    days, day = [], date(2025, 1, 6)
    while len(days) < sessions:
        if day.weekday() < 5:
            days.append(day.isoformat())
        day += timedelta(days=1)
    bars, quotes = [], []
    previous = {s: 80.0 + i * 20 for i, s in enumerate(SYMBOLS)}
    lag = {s: 0.0 for s in SYMBOLS}
    for day in days:
        common = rng.gauss(0, 0.004)
        for i, symbol in enumerate(SYMBOLS):
            mid = previous[symbol] * (1 + rng.gauss(0, 0.002))
            ret = 0.15 * lag[symbol] + common + rng.gauss(0, 0.006)
            close = mid * (1 + ret)
            bars.append(dict(symbol=symbol, event_at=day + "T17:00:00+00:00",
                             available_at=day + "T17:05:00+00:00", version=1,
                             mid=mid, close=close))
            quotes.append(dict(symbol=symbol, at=day + "T16:00:00+00:00",
                               mid=mid, close=close, spread_bps=4.0 + i * 2,
                               interval_volume=1000 + 100 * i))
            previous[symbol], lag[symbol] = close, ret
    return {"data_kind": "synthetic; weekday calendar is NOT an exchange calendar",
            "seed": seed, "days": days, "bars": bars, "quotes": quotes}


def validate_bars(rows: list[dict]) -> None:
    seen = set()
    for r in rows:
        key = (r["symbol"], r["event_at"], r["version"])
        if key in seen:
            raise ValueError("duplicate bar version")
        seen.add(key)
        if not isinstance(r["symbol"], str) or not r["symbol"]:
            raise ValueError("invalid symbol")
        if type(r["version"]) is not int or r["version"] < 1:
            raise ValueError("invalid version")
        if timestamp(r["available_at"]) < timestamp(r["event_at"]):
            raise ValueError("bar available before event")
        for name in ("mid", "close"):
            if finite(r[name], name) <= 0:
                raise ValueError("nonpositive price")


def asof(rows: list[dict], cutoff: str) -> list[dict]:
    """Latest received revision of every event at this cutoff, never future rows."""
    now, selected = timestamp(cutoff), {}
    for r in rows:
        if timestamp(r["event_at"]) > now or timestamp(r["available_at"]) > now:
            continue
        key = (r["symbol"], r["event_at"])
        rank = (timestamp(r["available_at"]), r["version"])
        if key not in selected or rank > selected[key][0]:
            selected[key] = (rank, r)
    return [selected[k][1] for k in sorted(selected)]


def features(rows: list[dict], cutoff: str) -> dict[str, dict]:
    latest = {}
    for r in asof(rows, cutoff):
        symbol = r["symbol"]
        if symbol not in latest or timestamp(r["event_at"]) > timestamp(latest[symbol]["event_at"]):
            latest[symbol] = r
    return {s: dict(x=r["close"] / r["mid"] - 1, price=r["close"],
                    source_event=r["event_at"], available_at=r["available_at"],
                    version=r["version"]) for s, r in latest.items()}
