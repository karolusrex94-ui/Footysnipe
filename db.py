import sqlite3
import json
from datetime import datetime

DB_NAME = "footsnipe.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            home_name TEXT,
            away_name TEXT,
            result_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_prediction(home_name, away_name, result_data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO predictions (timestamp, home_name, away_name, result_data)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now().isoformat(), home_name, away_name, json.dumps(result_data)))
    conn.commit()
    conn.close()
