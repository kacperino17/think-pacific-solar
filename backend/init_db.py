# init_db.py

import sqlite3

def create_tables():
    conn = sqlite3.connect("backend/aircast.db")
    cursor = conn.cursor()

    # Table 1: Raw pollutant data and AQI
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pollutants_aqi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            pm25 REAL,
            pm10 REAL,
            co REAL,
            o3 REAL,
            no2 REAL,
            so2 REAL,
            aqi_pm25 INTEGER,
            aqi_pm10 INTEGER,
            aqi_co INTEGER,
            aqi_o3 INTEGER,
            aqi_no2 INTEGER,
            aqi_so2 INTEGER,
            total_aqi INTEGER
        );
    """)

    # Table 2: Final hourly AQI with weather modifiers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS month_01_database (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            original_aqi INTEGER,
            adjusted_aqi REAL,
            wind_speed REAL,
            humidity REAL,
            rainfall REAL,
            pressure REAL
        );
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
