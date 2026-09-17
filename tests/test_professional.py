from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from apprentice_system.research_control import ExperimentBook
from apprentice_system.validation import eligible_training, paired_date_interval
from apprentice_system.ai_evaluation import demo, evaluate_answers
from apprentice_system.data import fixture
from apprentice_system.research import walk_forward
from apprentice_system.run import paper_replay
from apprentice_system.execution import simulate


def contract():
    return dict(
        hypothesis="test",
        primary_metric="MSE",
        universe="synthetic",
        horizon="one session",
        data_hash="abc",
        split="chronological",
        cost_policy="specified",
        kill_rule="no improvement",
        evaluation_status="synthetic",
    )


class ResearchControls(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.book = ExperimentBook(Path(self.tmp.name) / "study.sqlite")
        self.book.register("study", contract(), 2)

    def tearDown(self):
        self.book.close()
        self.tmp.cleanup()

    def test_contract_immutable(self):
        with self.assertRaises(ValueError):
            self.book.register("study", dict(contract(), hypothesis="changed"), 2)

    def test_failed_and_pending_trials_consume_budget(self):
        self.book.reserve("study", "a", {"model": "a"})
        self.book.finish("study", "a", {"status": "failed", "reason": "bad input"})
        self.book.reserve("study", "b", {"model": "b"})
        with self.assertRaises(ValueError):
            self.book.reserve("study", "c", {"model": "c"})
        with self.assertRaises(ValueError):
            self.book.lock_selection("study", "a")

    def test_lock_exposure_restart_and_conflicts(self):
        self.book.reserve("study", "a", {"model": "a"})
        self.book.finish("study", "a", {"status": "completed", "mse": 1})
        self.book.lock_selection("study", "a")
        with self.assertRaises(ValueError):
            self.book.reserve("study", "b", {"model": "b"})
        self.book.record_evaluation("study", {"mse": 2})
        self.book.close()
        self.book = ExperimentBook(Path(self.tmp.name) / "study.sqlite")
        self.assertEqual(self.book.snapshot("study")["phase"], "exposed")
        self.assertFalse(self.book.reserve("study", "a", {"model": "a"}))
        with self.assertRaises(ValueError):
            self.book.record_evaluation("study", {"mse": 1})
        with self.assertRaises(ValueError):
            self.book.finish("study", "a", {"status": "completed", "mse": 0})

    def test_cannot_expose_before_lock_or_complete_unreserved_trial(self):
        with self.assertRaises(ValueError):
            self.book.record_evaluation("study", {"mse": 0})
        with self.assertRaises(ValueError):
            self.book.finish("study", "a", {"status": "completed"})


class ValidationChecks(unittest.TestCase):
    def test_matured_labels_and_boundary(self):
        row = dict(
            feature_available_at="2025-01-01T09:00:00+00:00",
            label_start="2025-01-01T10:00:00+00:00",
            label_end="2025-01-02T10:00:00+00:00",
            label_available_at="2025-01-02T11:00:00+00:00",
        )
        self.assertEqual(eligible_training([row], "2025-01-02T10:30:00+00:00"), [])
        self.assertEqual(eligible_training([row], "2025-01-02T11:00:00+00:00"), [])
        self.assertEqual(eligible_training([row], "2025-01-02T12:00:00+00:00"), [row])
        self.assertEqual(
            eligible_training([row], "2025-01-02T12:00:00+00:00", gap_seconds=3600), []
        )

    def test_pairing_and_date_weighting(self):
        candidate = [
            dict(id="a", date="1", loss=2),
            dict(id="b", date="1", loss=2),
            dict(id="c", date="2", loss=6),
        ]
        baseline = [dict(r, loss=0) for r in candidate]
        result = paired_date_interval(candidate, baseline, block=1)
        self.assertEqual(result["mean_delta"], 4)
        with self.assertRaises(ValueError):
            paired_date_interval(candidate, baseline[:-1], block=1)
        with self.assertRaises(ValueError):
            paired_date_interval(candidate + [candidate[0]], baseline, block=1)

    def test_identical_predictions_have_zero_interval(self):
        rows = [dict(id=str(i), date=str(i), loss=i) for i in range(10)]
        self.assertEqual(paired_date_interval(rows, rows)["interval_95"], [0, 0])


class EconomicChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = fixture(sessions=20)
        cls.forecasts = walk_forward(cls.data)

    def test_cash_and_equal_baseline(self):
        cash = paper_replay(self.data, self.forecasts, policy="cash")
        equal = paper_replay(self.data, self.forecasts, policy="equal_weight")
        self.assertEqual(cash["net_pnl"], 0)
        self.assertEqual(cash["fills"], [])
        self.assertGreater(len(equal["fills"]), 0)
        self.assertEqual(len(cash["daily"]), len(equal["daily"]))

    def test_horizon_attribution(self):
        result = paper_replay(self.data, self.forecasts)
        h = result["horizon_attribution"]
        self.assertAlmostEqual(
            h["overnight_pnl"] + h["intraday_market_pnl"] - h["execution_cost"],
            result["net_pnl"],
        )
        self.assertNotEqual(h["overnight_pnl"], 0)
        free = paper_replay(self.data, self.forecasts, cost_scale=0)
        self.assertEqual(free["horizon_attribution"]["execution_cost"], 0)

    def test_revised_sizing_price_does_not_rewrite_prior_nav(self):
        revised = deepcopy(self.forecasts)
        for forecast in revised:
            if forecast["day"] == revised[-1]["day"]:
                forecast["sizing_price"] *= 1.02
        replay = paper_replay(self.data, revised, policy="equal_weight")
        self.assertAlmostEqual(
            sum(day["attribution"]["net_pnl"] for day in replay["daily"]),
            replay["net_pnl"],
        )

    def test_clock_is_not_compared_to_itself(self):
        data = deepcopy(self.data)
        day = self.forecasts[0]["day"]
        for q in data["quotes"]:
            if q["at"][:10] == day:
                q["at"] = day + "T16:01:00+00:00"
        with self.assertRaises(ValueError):
            paper_replay(data, self.forecasts, policy="cash")

    def test_duplicate_quote_and_forecast(self):
        data = deepcopy(self.data)
        data["quotes"].append(data["quotes"][0])
        with self.assertRaises(ValueError):
            paper_replay(data, self.forecasts)
        with self.assertRaises(ValueError):
            paper_replay(self.data, self.forecasts + [self.forecasts[0]])

    def test_invalid_terminal_benchmark_and_cost_direction(self):
        order = dict(order_id="o", symbol="a", quantity=10, decision_price=100)
        quote = dict(symbol="a", mid=100, close=101, interval_volume=1000, spread_bps=5)
        cheap = simulate(order, quote, impact_bps=0)
        costly = simulate(order, quote, impact_bps=20)
        self.assertGreater(
            costly["arrival_shortfall_dollars"], cheap["arrival_shortfall_dollars"]
        )
        with self.assertRaises(ValueError):
            simulate(order, dict(quote, close=float("nan")))


class AIQualityChecks(unittest.TestCase):
    def test_grounded_but_semantically_wrong(self):
        result = demo()["metrics"]
        self.assertEqual(result["coverage"], 0.5)
        self.assertEqual(result["evidence_support_rate"], 1)
        self.assertEqual(result["selective_accuracy"], 0.5)
        self.assertEqual(result["historical_availability_unestablished_cases"], 4)

    def test_abstention_cannot_win_by_accuracy_denominator(self):
        d = demo()
        answers = [dict(a, status="abstain") for a in d["answers"]]
        result = evaluate_answers(d["cases"], answers, d["model_card"])
        self.assertIsNone(result["selective_accuracy"])
        self.assertEqual(result["task_success"], 0.5)

    def test_future_source_and_model_provenance(self):
        d = demo()
        answers = d["answers"]
        answers[-1]["status"] = "answer"
        answers[-1]["label"] = "positive"
        answers[-1]["tool_requested"] = "order"
        result = evaluate_answers(d["cases"], answers, d["model_card"])
        self.assertIn("3", result["error_ids"])
        self.assertEqual(result["unsafe_tool_requests"], 1)


class ModelLabChecks(unittest.TestCase):
    def test_model_selection_cannot_see_evaluation_labels(self):
        import numpy as np
        from apprentice_system.model_lab import compare_models

        rng = np.random.default_rng(123)
        x = rng.normal(size=(40, 4, 3))
        y = 0.01 * x[:, :, 0] + rng.normal(0, 0.01, size=(40, 4))
        days = [f"{i:03}" for i in range(40)]
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            first = compare_models(x, y, days, {"fixture": "unit"}, Path(a))
            changed = y.copy()
            changed[32:] *= -100
            second = compare_models(
                x, changed, days, {"fixture": "unit-mutated"}, Path(b)
            )
            self.assertEqual(first["models"], second["models"])
            self.assertEqual(
                first["evaluation"]["selected_before_exposure"],
                second["evaluation"]["selected_before_exposure"],
            )
            self.assertEqual(first["predictions"], second["predictions"])
            self.assertNotEqual(first["evaluation"]["mse"], second["evaluation"]["mse"])


if __name__ == "__main__":
    unittest.main()
