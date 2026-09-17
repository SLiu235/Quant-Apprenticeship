"""Deterministic temporal retrieval baseline, not a live LLM."""
import re
from .core import timestamp

DOCUMENTS = [
    dict(id="research-policy", available_at="2025-01-01T00:00:00+00:00",
         text="Forecast quality is compared with a zero-return baseline using squared error."),
    dict(id="execution-policy", available_at="2025-01-01T00:00:00+00:00",
         text="Execution costs include spread, stipulated impact and fees. Unfilled quantities are cancelled."),
    dict(id="future-policy", available_at="2030-01-01T00:00:00+00:00",
         text="Execution costs are waived in this fictional future policy."),
]


def retrieve(query: str, cutoff: str, documents: list[dict] = DOCUMENTS) -> dict:
    tokens = set(re.findall(r"[a-z]+", query.lower())) - {"the", "a", "is", "what", "are", "and"}
    candidates = []
    for doc in documents:
        if timestamp(doc["available_at"]) <= timestamp(cutoff):
            overlap = tokens & set(re.findall(r"[a-z]+", doc["text"].lower()))
            if overlap:
                candidates.append((len(overlap), doc["id"], doc))
    if not candidates:
        return {"status": "abstain", "reason": "no lexical evidence", "citations": []}
    doc = sorted(candidates, key=lambda x: (-x[0], x[1]))[0][2]
    return {"status": "evidence", "quote": doc["text"], "citations": [doc["id"]],
            "available_at": doc["available_at"], "scope": "retrieved text, not an inferred answer or trade instruction"}


def evidence_valid(answer: dict, cutoff: str, documents: list[dict] = DOCUMENTS) -> bool:
    if answer.get("status") == "abstain":
        return answer.get("citations") == []
    if answer.get("status") != "evidence" or len(answer.get("citations", [])) != 1:
        return False
    return any(d["id"] == answer["citations"][0] and bool(answer.get("quote"))
               and answer["quote"] in d["text"] and timestamp(d["available_at"]) <= timestamp(cutoff)
               for d in documents)
