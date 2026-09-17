"""Content-addressed artifacts and transactional local event persistence."""
import json
import os
from pathlib import Path
import sqlite3
import tempfile
from .core import encoded, fingerprint


def artifact(directory: Path, value: object) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / (fingerprint(value) + ".json")
    payload = encoded(value)
    fd, temporary = tempfile.mkstemp(dir=directory, prefix=".pending-")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)  # publish a complete file without replacing another writer
        except FileExistsError:
            if path.read_bytes() != payload:
                raise ValueError("existing artifact is corrupt; refuse silent reuse")
    finally:
        Path(temporary).unlink(missing_ok=True)
    return path


class EventStore:
    def __init__(self, path: Path):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS events (seq INTEGER PRIMARY KEY, id TEXT UNIQUE NOT NULL, payload TEXT NOT NULL)")
        self.db.commit()

    def append(self, event_id: str, event: dict) -> bool:
        payload = encoded(event).decode()
        with self.db:
            cursor = self.db.execute("INSERT OR IGNORE INTO events(id,payload) VALUES (?,?)", (event_id, payload))
            stored = self.db.execute("SELECT payload FROM events WHERE id=?", (event_id,)).fetchone()[0]
            if stored != payload:
                raise ValueError("conflicting event ID")
            return cursor.rowcount == 1

    def events(self) -> list[dict]:
        return [json.loads(row[0]) for row in self.db.execute("SELECT payload FROM events ORDER BY seq")]

    def close(self) -> None:
        self.db.close()
