from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from apprentice_system.core import timestamp
from apprentice_system.data import asof, features, fixture, validate_bars
from apprentice_system.research import walk_forward
from apprentice_system.portfolio import weights, orders
from apprentice_system.risk import attribution, check_weights, scenarios
from apprentice_system.execution import Ledger, simulate, twap
from apprentice_system.pipeline import EventStore, artifact
from apprentice_system.copilot import retrieve, evidence_valid
from apprentice_system.monitoring import alerts
from apprentice_system.run import run


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = fixture(sessions=20)

    def test_reject_naive_clock(self):
        with self.assertRaises(ValueError):
            timestamp("2025-01-01T12:00:00")

    def test_duplicate_and_nonfinite(self):
        with self.assertRaises(ValueError):
            validate_bars(self.data["bars"] + [self.data["bars"][0]])
        self.data["bars"][0]["close"] = float("nan")
        with self.assertRaises(ValueError):
            validate_bars(self.data["bars"])

    def test_revision_cannot_change_prior_view(self):
        cutoff = self.data["days"][1] + "T15:55:00+00:00"
        old = features(self.data["bars"], cutoff)
        revised = dict(self.data["bars"][0], version=2, close=999,
                       available_at=self.data["days"][2]+"T17:05:00+00:00")
        self.data["bars"].append(revised)
        self.assertEqual(old, features(self.data["bars"], cutoff))
        later = asof(self.data["bars"], revised["available_at"])
        self.assertIn(revised, later)

    def test_future_price_mutation_keeps_earlier_forecasts(self):
        original = walk_forward(self.data)
        cutoff_day = self.data["days"][12]
        for r in self.data["bars"]:
            if r["event_at"][:10] >= cutoff_day:
                r["close"] *= 3
        changed = walk_forward(self.data)
        self.assertEqual([f for f in original if f["day"] <= cutoff_day],
                         [f for f in changed if f["day"] <= cutoff_day])

    def test_training_labels_precede_decision(self):
        forecasts = walk_forward(self.data)
        self.assertGreater(len(forecasts), 0)
        for f in forecasts:
            self.assertLess(timestamp(f["latest_training_label"]), timestamp(f["decision_at"]))
            self.assertLess(timestamp(f["feature_available_at"]), timestamp(f["decision_at"]))


class PortfolioTests(unittest.TestCase):
    def test_zero_and_negative_forecast_keep_cash(self):
        self.assertEqual(weights({"a": -1, "b": 0}), {"a": 0, "b": 0})

    def test_concentration_and_gross(self):
        w = weights({str(i): 1 for i in range(10)})
        check_weights(w)
        self.assertAlmostEqual(sum(w.values()), .8)
        with self.assertRaises(ValueError):
            check_weights({"a": .4})

    def test_sizing_and_liquidation(self):
        result = orders({"a": .25}, {"a": 30, "b": 2}, 1000, {"a": 10, "b": 5}, "x")
        self.assertEqual({r["symbol"]: r["quantity"] for r in result}, {"a": -5, "b": -2})

    def test_scenario_units_and_coverage(self):
        self.assertAlmostEqual(scenarios({"a": .25}, {"shock": {"a": -.2}})["shock"], -.05)
        with self.assertRaises(ValueError):
            scenarios({"a": .25}, {"shock": {}})


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.order = dict(order_id="o", symbol="a", quantity=100, decision_price=100.0)
        self.quote = dict(symbol="a", mid=100.0, close=101.0, spread_bps=10.0, interval_volume=500)

    def test_partial_fill_and_shortfall(self):
        r = simulate(self.order, self.quote, participation=.1, impact_bps=0, fee_per_share=.01)
        self.assertEqual((r["filled"], r["cancelled"]), (50, 50))
        self.assertAlmostEqual(r["fill"]["price"], 100.05)
        self.assertAlmostEqual(r["arrival_shortfall_dollars"], 3.0)
        self.assertAlmostEqual(r["unfilled_opportunity_dollars"], 50.0)

    def test_sell_sign_and_empty_market(self):
        self.order["quantity"] = -100
        r = simulate(self.order, self.quote, impact_bps=0)
        self.assertLess(r["fill"]["price"], 100)
        self.assertGreater(r["arrival_shortfall_dollars"], 0)
        self.quote["interval_volume"] = 0
        self.assertIsNone(simulate(self.order, self.quote)["fill"])

    def test_duplicate_and_conflict(self):
        ledger, fill = Ledger(), simulate(self.order, self.quote)["fill"]
        self.assertTrue(ledger.apply(fill))
        cash = ledger.cash
        self.assertFalse(ledger.apply(fill))
        self.assertEqual(cash, ledger.cash)
        with self.assertRaises(ValueError):
            ledger.apply(dict(fill, price=fill["price"] + 1))

    def test_reject_unfunded_or_short_fill(self):
        fill = simulate(self.order, self.quote)["fill"]
        with self.assertRaises(ValueError):
            Ledger(cash=1).apply(fill)
        with self.assertRaises(ValueError):
            Ledger().apply(dict(fill, quantity=-1))

    def test_accounting_hand_example(self):
        ledger = Ledger(cash=1000, holdings={"a": 2})
        before = ledger.equity({"a": 100})
        fill = dict(fill_id="f", symbol="a", quantity=3, price=101.0, fee=1.0)
        ledger.apply(fill)
        after = ledger.equity({"a": 102})
        explanation = attribution({"a": 2}, {"a": 100}, {"a": 102}, [fill])
        self.assertAlmostEqual(after - before, 6.0)
        self.assertAlmostEqual(explanation["net_pnl"], 6.0)

    def test_twap_conservation(self):
        self.assertEqual(twap(103, 4), [26, 26, 26, 25])
        self.assertEqual(sum(twap(-103, 4)), -103)


class OperationTests(unittest.TestCase):
    def test_artifact_corruption_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = artifact(Path(tmp), {"a": 1})
            self.assertEqual(path, artifact(Path(tmp), {"a": 1}))
            path.write_text("corrupt")
            with self.assertRaises(ValueError):
                artifact(Path(tmp), {"a": 1})

    def test_persistent_idempotency(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.sqlite"
            store = EventStore(path)
            self.assertTrue(store.append("f", {"q": 1}))
            store.close()
            store = EventStore(path)
            try:
                self.assertFalse(store.append("f", {"q": 1}))
                with self.assertRaises(ValueError):
                    store.append("f", {"q": 2})
                self.assertEqual(store.events(), [{"q": 1}])
            finally:
                store.close()

    def test_retrieval_time_abstention_and_fabrication(self):
        cutoff = "2025-06-01T00:00:00+00:00"
        answer = retrieve("execution costs", cutoff)
        self.assertEqual(answer["citations"], ["execution-policy"])
        self.assertTrue(evidence_valid(answer, cutoff))
        self.assertFalse(evidence_valid(dict(answer, quote="profit guaranteed"), cutoff))
        self.assertEqual(retrieve("zebra", cutoff)["status"], "abstain")

    def test_alerts(self):
        now = "2025-01-01T16:00:00+00:00"
        self.assertEqual(alerts(now, now, 100, 100, .5, .2), [])
        self.assertIn("pnl_reconciliation_failure", alerts(now, now, 100, 101, .5, .2))
        self.assertIn("post_fill_exposure_breach", alerts(now, now, 100, 100, .9, .4))
        self.assertIn("invalid_numeric_state", alerts(now, now, float("nan"), 100, .5, .2))

    def test_full_pipeline_and_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run(10, Path(tmp))
            again = run(10, Path(tmp))
            self.assertEqual(result, again)
            self.assertEqual(len(result), 10)
            self.assertTrue(result[7]["restart_matches"])
            self.assertGreater(result[7]["persisted_fills"], 0)
            self.assertLess(result[10]["max_accounting_residual"], 1e-7)
            self.assertAlmostEqual(sum(d["attribution"]["net_pnl"] for d in result[6]["replay"]["daily"]), result[10]["net_pnl"])


if __name__ == "__main__":
    unittest.main()
