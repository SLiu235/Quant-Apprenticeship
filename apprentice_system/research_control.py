"""Local, transactional experiment commitments; not a tamperproof audit service."""

import json
from pathlib import Path
import sqlite3
from .core import encoded, fingerprint


class ExperimentBook:
    """Reserve attempts before compute; lock selection before evaluation exposure.

    Prompts/features/seeds count as trials if they influence selection. This API
    records declared usage; it cannot prevent off-book research or file access.
    """

    def __init__(self, path: Path):
        self.db = sqlite3.connect(path)
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS studies (
          id TEXT PRIMARY KEY, protocol TEXT NOT NULL, budget INTEGER NOT NULL,
          phase TEXT NOT NULL, selected TEXT, evaluation TEXT);
        CREATE TABLE IF NOT EXISTS trials (
          study TEXT NOT NULL, id TEXT NOT NULL, specification TEXT NOT NULL,
          result TEXT, PRIMARY KEY(study, id));
        """)
        self.db.commit()

    def register(self, study_id: str, protocol: dict, budget: int) -> None:
        required = {
            "hypothesis",
            "primary_metric",
            "universe",
            "horizon",
            "data_hash",
            "split",
            "cost_policy",
            "kill_rule",
            "evaluation_status",
        }
        if required - set(protocol) or any(not protocol[k] for k in required):
            raise ValueError("incomplete research contract")
        if protocol["evaluation_status"] not in {
            "synthetic",
            "inspected_development",
            "prospective_pending",
        }:
            raise ValueError("unsupported evidence status")
        if type(budget) is not int or budget < 1:
            raise ValueError("positive integer budget required")
        payload = encoded(protocol).decode()
        with self.db:
            self.db.execute(
                "INSERT OR IGNORE INTO studies VALUES (?,?,?,'development',NULL,NULL)",
                (study_id, payload, budget),
            )
            row = self.db.execute(
                "SELECT protocol,budget FROM studies WHERE id=?", (study_id,)
            ).fetchone()
            if row != (payload, budget):
                raise ValueError("study already committed with different contract")

    def reserve(self, study_id: str, trial_id: str, specification: dict) -> bool:
        payload = encoded(specification).decode()
        try:
            self.db.execute("BEGIN IMMEDIATE")
            study = self.db.execute(
                "SELECT budget,phase FROM studies WHERE id=?", (study_id,)
            ).fetchone()
            if not study:
                raise ValueError("unknown study")
            existing = self.db.execute(
                "SELECT specification FROM trials WHERE study=? AND id=?",
                (study_id, trial_id),
            ).fetchone()
            if existing:
                if existing[0] != payload:
                    raise ValueError("conflicting trial identity")
                self.db.commit()
                return False
            if study[1] != "development":
                raise ValueError(
                    "selection locked; new trials need a new development study"
                )
            count = self.db.execute(
                "SELECT COUNT(*) FROM trials WHERE study=?", (study_id,)
            ).fetchone()[0]
            if count >= study[0]:
                raise ValueError("trial budget exhausted; failed attempts still count")
            self.db.execute(
                "INSERT INTO trials VALUES (?,?,?,NULL)", (study_id, trial_id, payload)
            )
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise

    def finish(self, study_id: str, trial_id: str, result: dict) -> None:
        if result.get("status") not in {"completed", "failed"}:
            raise ValueError("trial requires completed or failed status")
        payload = encoded(result).decode()
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            row = self.db.execute(
                "SELECT result FROM trials WHERE study=? AND id=?", (study_id, trial_id)
            ).fetchone()
            if not row:
                raise ValueError("trial must be reserved before computation")
            if row[0] is not None:
                if row[0] != payload:
                    raise ValueError("completed trial is immutable")
                return
            phase = self.db.execute(
                "SELECT phase FROM studies WHERE id=?", (study_id,)
            ).fetchone()[0]
            if phase != "development":
                raise ValueError("study is locked")
            self.db.execute(
                "UPDATE trials SET result=? WHERE study=? AND id=?",
                (payload, study_id, trial_id),
            )

    def lock_selection(self, study_id: str, trial_id: str) -> None:
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            study = self.db.execute(
                "SELECT phase,selected FROM studies WHERE id=?", (study_id,)
            ).fetchone()
            if not study:
                raise ValueError("unknown study")
            if study[0] != "development":
                if study[1] != trial_id:
                    raise ValueError("selection already locked")
                return
            rows = self.db.execute(
                "SELECT id,result FROM trials WHERE study=?", (study_id,)
            ).fetchall()
            if any(result is None for _, result in rows):
                raise ValueError(
                    "unresolved trials must be recorded, including failures"
                )
            selected = dict(rows).get(trial_id)
            if not selected or json.loads(selected)["status"] != "completed":
                raise ValueError("selected trial must have a completed result")
            self.db.execute(
                "UPDATE studies SET phase='locked', selected=? WHERE id=?",
                (trial_id, study_id),
            )

    def record_evaluation(self, study_id: str, evaluation: dict) -> None:
        payload = encoded(evaluation).decode()
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            row = self.db.execute(
                "SELECT phase,evaluation FROM studies WHERE id=?", (study_id,)
            ).fetchone()
            if not row or row[0] == "development":
                raise ValueError("lock selection before recording evaluation")
            if row[1] is not None and row[1] != payload:
                raise ValueError("evaluation already exposed; do not overwrite")
            self.db.execute(
                "UPDATE studies SET phase='exposed',evaluation=? WHERE id=?",
                (payload, study_id),
            )

    def snapshot(self, study_id: str) -> dict:
        row = self.db.execute(
            "SELECT protocol,budget,phase,selected,evaluation FROM studies WHERE id=?",
            (study_id,),
        ).fetchone()
        if not row:
            raise ValueError("unknown study")
        trials = self.db.execute(
            "SELECT id,specification,result FROM trials WHERE study=? ORDER BY id",
            (study_id,),
        ).fetchall()
        return dict(
            protocol=json.loads(row[0]),
            protocol_hash=fingerprint(json.loads(row[0])),
            budget=row[1],
            phase=row[2],
            selected=row[3],
            evaluation=json.loads(row[4]) if row[4] else None,
            trials=[
                dict(
                    id=t[0],
                    specification=json.loads(t[1]),
                    result=json.loads(t[2]) if t[2] else None,
                )
                for t in trials
            ],
        )

    def close(self) -> None:
        self.db.close()
