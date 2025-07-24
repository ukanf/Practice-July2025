import sqlite3
import json
from contextlib import contextmanager

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
                execution_time REAL NOT NULL
            )
        """)

def save_execution(execution):
    with get_db() as db:
        db.execute("""
            INSERT OR REPLACE INTO executions (id, workflow, state, current_step, step_output, engine_type, execution_time)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            execution["id"],
            execution["workflow"],
            execution["state"],
            execution.get("current_step"),
            json.dumps(execution.get("step_output", {})),
            execution.get("engine_type"),
            execution.get("execution_time"),
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
                "execution_time": row["execution_time"]
            }
        return None
