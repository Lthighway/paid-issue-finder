"""Bound SQLite growth before GitHub commits; preserve observations and outbox."""
import sqlite3
import sys
import time
from pathlib import Path

MAX_BYTES = 90 * 1024 * 1024
KEEP_RUNS = 30

def maintain(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with sqlite3.connect(str(path), timeout=30) as db:
        result = db.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError("SQLite integrity check failed: " + result)
        db.execute("DELETE FROM runs WHERE id NOT IN (SELECT id FROM runs ORDER BY id DESC LIMIT ?)", (KEEP_RUNS,))
        db.execute("DELETE FROM cache WHERE ts < ?", (time.time() - 86400,))
        db.commit()
        db.execute("VACUUM")
        if path.stat().st_size > MAX_BYTES:
            # Cache is regenerable; observations and notification outbox are not.
            db.execute("DELETE FROM cache")
            db.execute("DELETE FROM runs WHERE id NOT IN (SELECT id FROM runs ORDER BY id DESC LIMIT 5)")
            db.commit()
            db.execute("VACUUM")
        result = db.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError("SQLite integrity check failed after maintenance: " + result)
    size = path.stat().st_size
    print(f"SQLite maintenance: {size / 1024 / 1024:.2f} MiB; limit {MAX_BYTES / 1024 / 1024:.0f} MiB", flush=True)
    if size > MAX_BYTES:
        raise RuntimeError("SQLite still too large: preserved observations/outbox; manual review needed")

if __name__ == "__main__":
    maintain(sys.argv[1] if len(sys.argv) > 1 else "treasure-state/monitor.sqlite")
