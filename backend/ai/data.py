# backend/ai/step1_data.py

import pandas as pd
import sqlite3
import os

def get_adjusted_aqi_series():
    db_path = os.path.join(os.path.dirname(__file__), "..", "aircast.db")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(
        "SELECT timestamp, adjusted_aqi FROM month_01_database ORDER BY timestamp ASC",
        conn
    )
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    conn.close()
    return df
