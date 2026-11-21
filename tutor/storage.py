"""SQLite storage for sessions, so we can show progress and prove learning."""
import sqlite3
import time

DB = "tutor.db"


def _conn():
    c = sqlite3.connect(DB)
    c.execute(
        "CREATE TABLE IF NOT EXISTS attempts ("
        "id INTEGER PRIMARY KEY, ts REAL, learner TEXT, topic TEXT, "
        "stage TEXT, score REAL, mastered INTEGER)"
    )
    return c


def save_attempt(learner: str, topic: str, stage: str, score: float, mastered: bool):
    with _conn() as c:
        c.execute(
            "INSERT INTO attempts (ts, learner, topic, stage, score, mastered) VALUES (?,?,?,?,?,?)",
            (time.time(), learner, topic, stage, score, int(mastered)),
        )


def history(learner: str):
    with _conn() as c:
        return c.execute(
            "SELECT ts, topic, stage, score, mastered FROM attempts WHERE learner=? ORDER BY ts",
            (learner,),
        ).fetchall()
