"""Known-MDP synthetic demonstrations, explicitly an oracle teaching experiment."""

import sys
import numpy as np
from scipy.optimize import minimize
from .common import WORKSPACE

sys.path.insert(0, str(WORKSPACE / "BehaviorIRL"))
from behavior_irl.mdp import (
    Mechanics,
    STATES,
    INDEX,
    MASK,
    transition,
    reward_features,
    plan,
)
from behavior_irl.models import irl_objective, fit_frequency, fit_bc, fit_irl


def demonstrate(lp, p, horizon, count, seed):
    rng = np.random.default_rng(seed)
    rows = []
    for episode in range(count):
        state = INDEX[(3, int(rng.choice([-1, 0, 1])), int(rng.integers(2)), 0)]
        for t in range(horizon):
            action = int(rng.choice(3, p=np.exp(lp[t, state])))
            nxt = int(rng.choice(len(STATES), p=p[state, action]))
            rows.append(
                {
                    "episode": str(episode),
                    "actor": "simulated",
                    "step": t,
                    "state": state,
                    "action": action,
                    "next_state": nxt,
                }
            )
            state = nxt
    return rows


def nll(lp, rows):
    active = [r for r in rows if STATES[r["state"], 0] > 0]
    return float(-np.mean([lp[r["step"], r["state"], r["action"]] for r in active]))


def run():
    m = Mechanics()
    p = transition(m)
    phi = reward_features(p, m)
    theta = np.array([1.0, 0.12, 0.65, 1.4])
    lp, jac = plan(p, phi, theta, m.temperature, True)
    train = demonstrate(lp, p, m.horizon, 180, 41)
    test = demonstrate(lp, p, m.horizon, 80, 42)
    opt = minimize(
        irl_objective,
        [0.08, 0.4, 1.0],
        args=(train, p, phi, m.temperature, 0.0, None),
        jac=True,
        method="L-BFGS-B",
        bounds=[(0, 1), (0, 3), (0, 5)],
        options={"ftol": 1e-12, "maxiter": 200},
    )
    if not opt.success:
        raise RuntimeError(str(opt.message))
    recovered = np.r_[1.0, opt.x]
    fitlp = plan(p, phi, recovered, m.temperature)[0]
    scaled = plan(p, phi, 3 * theta, 3 * m.temperature)[0]
    eps = 1e-5
    direction = np.array([0.0, 0.0, eps, 0.0])
    valid = np.broadcast_to(MASK, lp.shape)
    plus = plan(p, phi, theta + direction, m.temperature)[0]
    minus = plan(p, phi, theta - direction, m.temperature)[0]
    error = float(
        np.max(
            np.abs((plus[valid] - minus[valid]) / (2 * eps) - jac[:, :, :, 2][valid])
        )
    )
    changed = Mechanics(passive_normal=0.35, passive_thin=0.10)
    cp = transition(changed)
    cf = reward_features(cp, changed)
    shifted = plan(cp, cf, theta, changed.temperature)[0]
    shift = demonstrate(shifted, cp, changed.horizon, 80, 43)
    adapted = plan(cp, cf, recovered, changed.temperature)[0]
    active = [row for row in test if STATES[row["state"], 0] > 0]

    def score_model(model):
        probabilities = model.probabilities(active)
        actions = np.array([row["action"] for row in active])
        return float(-np.log(probabilities[np.arange(len(active)), actions]).mean())

    frequency = fit_frequency(train, m.horizon)
    bc = fit_bc(train, m.horizon, mode="graph", penalty=0.01)
    empirical = fit_irl(train, m, penalty=0.01, hierarchical=False)
    if not bc.fit_status["success"] or not empirical.fit_status["success"]:
        raise RuntimeError("baseline or empirical dynamics fit failed")
    return {
        "frequency_test_nll": score_model(frequency),
        "behavior_cloning_test_nll": score_model(bc),
        "estimated_dynamics_irl_test_nll": score_model(empirical),
        "active_test_decisions": len(active),
        "data_kind": "synthetic known-MDP, no observed investor actions",
        "train_episodes": 180,
        "test_episodes": 80,
        "true_theta": theta.tolist(),
        "estimated_theta": recovered.tolist(),
        "test_nll_fit": nll(fitlp, test),
        "test_nll_oracle": nll(lp, test),
        "reward_temperature_scale_max_probability_error": float(
            np.max(np.abs(np.exp(lp) - np.exp(scaled)))
        ),
        "gradient_max_abs_error": error,
        "shift_nll_stale_policy": nll(fitlp, shift),
        "shift_nll_replanned_known_dynamics": nll(adapted, shift),
        "limits": "Fixed cost scale and temperature; oracle dynamics/reward family. Replanning assumes changed dynamics known.",
    }
