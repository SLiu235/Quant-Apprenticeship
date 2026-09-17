"""Small shared contracts; explicit units and UTC-aware clocks."""
from datetime import datetime
from hashlib import sha256
import json
import math
from pathlib import Path


def timestamp(value: str) -> datetime:
    result = datetime.fromisoformat(value)
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("timezone required")
    return result


def finite(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    return float(value)


def encoded(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()


def fingerprint(value: object) -> str:
    return sha256(encoded(value)).hexdigest()


def source_hashes() -> dict[str, str]:
    return {p.name: sha256(p.read_bytes()).hexdigest()
            for p in sorted(Path(__file__).parent.glob("*.py"))}


def research_contract() -> dict:
    return {
        "question": "Can a lagged synthetic return forecast improve squared error over zero?",
        "population": "AAA, BBB, CCC in an invented session calendar",
        "decision": "15:55 UTC; order sizing uses prior available close",
        "execution": "16:00 UTC synthetic quote, observed by simulator only",
        "target": "16:00 midpoint to 17:00 close return; decimal units",
        "baseline": "zero return; also report persistence forecast",
        "validation": "expanding fit using labels available strictly before each decision",
        "falsification": "no error improvement or an information-clock violation",
        "investment_scope": "software demonstration, no evidence of market alpha",
        "portfolio_scope": "long-only, cash residual, integer shares, no leverage",
    }
