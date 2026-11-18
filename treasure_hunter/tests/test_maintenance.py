import sqlite3
import tempfile
import unittest
from pathlib import Path

from treasure_hunter.maintenance import maintain

class MaintenanceTests(unittest.TestCase):
    def test_preserves_observations_and_outbox(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "monitor.sqlite"
            with sqlite3.connect(path) as db:
                db.executescript("""
                    CREATE TABLE runs(id INTEGER PRIMARY KEY, at TEXT, payload TEXT);
                    CREATE TABLE cache(key TEXT PRIMARY KEY, ts REAL, body TEXT);
                    CREATE TABLE observations(id TEXT PRIMARY KEY, fingerprint TEXT, payload TEXT, last_seen TEXT);
                    CREATE TABLE outbox(id TEXT PRIMARY KEY, payload TEXT, channels TEXT DEFAULT '[]', sent INTEGER DEFAULT 0);
                """)
                db.executemany("INSERT INTO runs(id,at,payload) VALUES(?,?,?)",
                               [(i, "today", "{}") for i in range(1, 51)])
                db.execute("INSERT INTO observations VALUES('item','hash','{}','today')")
                db.execute("INSERT INTO outbox(id,payload) VALUES('notice','{}')")
                db.execute("INSERT INTO cache VALUES('stale',0,'{}')")
            maintain(path)
            with sqlite3.connect(path) as db:
                self.assertEqual(db.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 30)
                self.assertEqual(db.execute("SELECT MIN(id) FROM runs").fetchone()[0], 21)
                self.assertEqual(db.execute("SELECT COUNT(*) FROM observations").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT COUNT(*) FROM cache").fetchone()[0], 0)

if __name__ == "__main__":
    unittest.main()
