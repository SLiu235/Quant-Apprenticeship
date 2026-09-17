import tempfile
import unittest
from pathlib import Path
import numpy as np
from reference.common import (
    scores,
    recent_predictions,
    date_deltas,
    block_interval,
)
from reference.p02_replay import Passive, run as replay
from reference.p03_baseline import design, fit, predict
from reference.p04_text import run as text_run
from reference.p05_risk import allocate
from reference.p06_irl import run as irl_run
from reference.p07_operations import PaperDesk
from reference.solutions import (
    asof_versions,
    permitted_labels,
    importance_value,
    edge_counts,
    gradient_error,
    mlp_fit,
    mlp_predict,
    journal_append,
    journal_replay,
)


class StatisticalTests(unittest.TestCase):
    def test_hand_scores_and_class_order(self):
        result = scores([[0.2, 0.3, 0.5]], [2])
        self.assertAlmostEqual(result["nll"], np.log(2))
        self.assertAlmostEqual(result["brier"], 0.38)
        self.assertGreater(scores([[0.5, 0.3, 0.2]], [2])["nll"], result["nll"])
        with self.assertRaises(ValueError):
            scores([[0.5, 0.5, 0.5]], [2])

    def test_independent_real_metrics(self):
        _, m = recent_predictions()
        dates, d = date_deltas(m["public"], m["market"])
        self.assertEqual(len(dates), 52)
        self.assertAlmostEqual(d.mean(), 0.014649936286815102, places=12)
        self.assertAlmostEqual(
            scores(m["public"]["p"], m["public"]["y"])["nll"],
            0.9773730683130558,
            places=12,
        )
        self.assertTrue(
            np.allclose(
                block_interval(d),
                [0.0064225027336277385, 0.02457989876926054],
                atol=1e-12,
            )
        )

    def test_ridge_future_invariance(self):
        rng = np.random.default_rng(42)
        r = rng.normal(0, 0.01, (120, 4))
        changed = r.copy()
        changed[110:] += 100
        x, y = design(r)
        cx, cy = design(changed)
        first = fit(x[:60], y[:60], 0.1)
        second = fit(cx[:60], cy[:60], 0.1)
        np.testing.assert_array_equal(
            predict(first, x[60:70]), predict(second, cx[60:70])
        )

    def test_risk_constraints_and_feasible_comparator(self):
        s = np.diag([1.0, 4.0, 9.0, 16.0])
        w = allocate(s)
        equal = np.ones(4) / 4
        self.assertAlmostEqual(w.sum(), 1)
        self.assertTrue((w >= -1e-8).all() and (w <= 0.50000001).all())
        self.assertLessEqual(w @ s @ w, equal @ s @ equal + 1e-8)
        # The fixed .5 cap binds the first asset; remaining weights ∝ inverse variance.
        rest = 1 / np.array([4.0, 9.0, 16.0])
        rest = 0.5 * rest / rest.sum()
        np.testing.assert_allclose(w, np.r_[0.5, rest], atol=1e-5)

    def test_irl_derivative_and_invariance(self):
        result = irl_run()
        self.assertLess(result["gradient_max_abs_error"], 1e-6)
        self.assertLess(result["reward_temperature_scale_max_probability_error"], 1e-12)

    def test_mlp_gradient_and_checkpoint(self):
        self.assertLess(gradient_error(), 1e-6)
        rng = np.random.default_rng(2)
        x = rng.normal(size=(50, 3))
        y = x[:, 0] * 0.3
        model = mlp_fit(x[:30], y[:30], x[30:], y[30:], epochs=50)
        value = np.mean((mlp_predict(model, x[30:]) - y[30:]) ** 2)
        self.assertAlmostEqual(value, model["validation_mse"])

    def test_importance_support(self):
        result = importance_value([1, 0, 3, 2], [1, 0, 1, 0], [0.5] * 4, True)
        self.assertEqual(result["value"], 2)
        self.assertEqual(result["ess"], 2)
        self.assertIsNone(importance_value([1], [1], [0.5], False)["value"])


class TemporalTests(unittest.TestCase):
    def test_version_asof(self):
        rows = [
            {
                "document_id": "a",
                "version_id": "1",
                "available_at": "2026-01-05T09:20:00-05:00",
                "text": "original",
            },
            {
                "document_id": "a",
                "version_id": "2",
                "available_at": "2026-01-05T09:26:00-05:00",
                "text": "revision",
            },
            {
                "document_id": "b",
                "version_id": "1",
                "available_at": "2026-01-05T09:24:00-05:00",
                "text": "other",
            },
        ]
        self.assertEqual(
            [r["text"] for r in asof_versions(rows, "2026-01-05T14:25:00+00:00")],
            ["original", "other"],
        )
        with self.assertRaises(ValueError):
            asof_versions(rows + rows[:1], "2026-01-05T14:25:00+00:00")
        with self.assertRaises(ValueError):
            asof_versions(rows, "2026-01-05T14:25:00")

    def test_purge_boundary_and_arrival(self):
        rows = [
            {
                "start": "2026-01-08T00:00:00+00:00",
                "end": "2026-01-12T00:00:00+00:00",
                "available_at": "2026-01-12T01:00:00+00:00",
            }
        ]
        self.assertEqual(permitted_labels(rows, "2026-01-10T00:00:00+00:00"), [])
        self.assertEqual(
            permitted_labels(
                rows,
                "2026-01-15T00:00:00+00:00",
                [("2026-01-12T00:00:00+00:00", "2026-01-14T00:00:00+00:00")],
            ),
            [],
        )

    def test_graph_unknown_not_zero(self):
        rows = [{"type": "reply", "available_at": "2026-01-05T14:26:00+00:00"}]
        self.assertIsNone(
            edge_counts(rows, "2026-01-05T14:25:00+00:00", False)["counts"]
        )
        self.assertEqual(
            edge_counts(rows, "2026-01-05T14:25:00+00:00", True)["counts"], {}
        )

    def test_text_clock_and_grounding(self):
        result = text_run()
        self.assertNotIn("e", result["eligible_ids"])
        self.assertEqual(result["rejected_evidence_ids"], ["f"])
        self.assertEqual(result["semantic_error_ids"], ["a"])
        self.assertAlmostEqual(result["accepted_accuracy"], 2 / 3)


class ExecutionTests(unittest.TestCase):
    def test_queue_conservation_and_shortfall(self):
        order = Passive(40, 40)
        order.trade(25)
        order.trade(30)
        order.cancel()
        self.assertEqual(order.filled + order.cancelled + order.remaining, 40)
        self.assertEqual(order.filled, 15)
        self.assertAlmostEqual(replay()["shortfall_dollars"], 0.36)

    def test_duplicate_fill_and_halt_reconciliation(self):
        desk = PaperDesk()
        desk.submit("o", 40, 1)
        desk.fill("f", "o", 15, 100.0)
        before = (desk.cash, desk.shares)
        desk.fill("f", "o", 15, 100.0)
        self.assertEqual(before, (desk.cash, desk.shares))
        desk.submit("bad", 10, 2000)
        desk.fill("g", "o", 25, 100.04)
        self.assertEqual((desk.cash, desk.shares), (5999.0, 40))
        self.assertFalse(desk.resume(True, 1))
        self.assertFalse(desk.reconcile(41, 5999.0, {"o": 0}))
        self.assertFalse(desk.resume(True, 1))
        self.assertTrue(desk.reconcile(40, 5999.0, {"o": 0}))
        self.assertTrue(desk.resume(True, 1))

    def test_conflicting_duplicate_and_nonfinite_quote(self):
        desk = PaperDesk()
        desk.submit("o", 40, 1)
        desk.fill("f", "o", 15, 100.0)
        before = (desk.cash, desk.shares)
        self.assertEqual(desk.fill("f", "o", 16, 100.0), "conflicting_fill_halt")
        self.assertEqual(before, (desk.cash, desk.shares))
        self.assertTrue(desk.halted)
        fresh = PaperDesk()
        self.assertEqual(fresh.submit("o", 1, float("nan")), "stale_quote_halt")

    def test_overfill_no_financial_mutation(self):
        desk = PaperDesk()
        desk.submit("o", 10, 1)
        self.assertEqual(desk.fill("f", "o", 11, 100), "invalid_fill_halt")
        self.assertEqual((desk.cash, desk.shares, desk.orders["o"]), (10000, 0, 10))
        self.assertTrue(desk.halted)

    def test_journal_replay_idempotence_and_corruption(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "journal.jsonl"
            event = {"id": "1", "quantity": 15}
            journal_append(path, event)
            journal_append(path, event)
            first = []
            second = []
            self.assertEqual(journal_replay(path, first.append), 1)
            journal_replay(path, second.append)
            self.assertEqual(first, second)
            journal_append(path, {"id": "1", "quantity": 16})
            with self.assertRaises(ValueError):
                journal_replay(path, lambda event: None)


if __name__ == "__main__":
    unittest.main()
