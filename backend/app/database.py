import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "energy_monitoring.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            voltage REAL NOT NULL,
            current REAL NOT NULL,
            power REAL NOT NULL,
            energy_kwh REAL NOT NULL,
            estimated_cost REAL NOT NULL,
            appliance TEXT NOT NULL,
            relay_status TEXT NOT NULL,
            alert_status TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def insert_reading(reading: dict):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO readings
        (timestamp, voltage, current, power, energy_kwh, estimated_cost, appliance, relay_status, alert_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            reading["timestamp"], reading["voltage"], reading["current"], reading["power"],
            reading["energy_kwh"], reading["estimated_cost"], reading["appliance"],
            reading["relay_status"], reading["alert_status"]
        ),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id


def fetch_readings(limit: int = 100):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM readings ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def latest_reading():
    conn = get_connection()
    row = conn.execute("SELECT * FROM readings ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return dict(row) if row else None


def clear_readings():
    conn = get_connection()
    conn.execute("DELETE FROM readings")
    conn.commit()
    conn.close()
