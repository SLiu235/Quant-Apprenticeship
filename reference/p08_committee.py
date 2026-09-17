"""Worked negative-result research decision."""

from .p01_audit import run as audit


def run():
    result = audit()
    return {
        "data_kind": "real saved result; decision exercise",
        "question": "Does frozen public text improve response probabilities over the market feature on eligible issuer-days?",
        "estimand": "Equal-weight date mean paired public-minus-market NLL",
        "evidence": result["primary"],
        "decision": "Do not promote this text model; retain negative exploratory result",
        "reason": "Primary difference positive; selection and timestamp gaps further restrict inference",
        "economic_claim": "None: no observed fills or calibrated payoff/cost model",
        "irl_claim": "None: actor state, actions and mandates unobserved",
        "next_experiment": "Prospectively freeze an independently acquired social/price availability panel and evaluate uninspected dates",
        "stop_rule": "Stop if receipt history, license or sampling cannot support claim; ordinary-session bars cannot substitute for overnight observations",
    }
