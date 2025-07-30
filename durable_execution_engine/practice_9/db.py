import sqlite3
import json
from contextlib import contextmanager
import time

@contextmanager
def get_db():
    conn = sqlite3.connect("workflow.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS executions (
                id TEXT PRIMARY KEY,
                workflow TEXT NOT NULL,
                state TEXT NOT NULL,
                current_step TEXT,
                step_output TEXT,
                engine_type TEXT NOT NULL,
                execution_time REAL NOT NULL,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL
            )
        """)

def save_execution(execution):
    now = time.time()
    with get_db() as db:
        # Check if execution exists to set created_at correctly
        row = db.execute("SELECT created_at FROM executions WHERE id = ?", (execution["id"],)).fetchone()
        if row:
            created_at = row["created_at"]
        else:
            created_at = now
        db.execute("""
            INSERT OR REPLACE INTO executions (
                id, workflow, state, current_step, step_output, engine_type, execution_time, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            execution["id"],
            execution["workflow"],
            execution["state"],
            execution.get("current_step"),
            json.dumps(execution.get("step_output", {})),
            execution.get("engine_type"),
            execution.get("execution_time"),
            created_at,
            now
        ))

def load_execution(execution_id):
    with get_db() as db:
        row = db.execute("SELECT * FROM executions WHERE id = ?", (execution_id,)).fetchone()
        if row:
            return {
                "id": row["id"],
                "workflow": row["workflow"],
                "state": row["state"],
                "current_step": row["current_step"],
                "step_output": json.loads(row["step_output"]) if row["step_output"] else {},
                "engine_type": row["engine_type"],
                "execution_time": row["execution_time"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
        return None
