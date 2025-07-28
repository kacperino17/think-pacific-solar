# main.py

import sqlite3
from datetime import datetime
from aqi_utils import compute_aqi, AQI_BREAKPOINTS

def process_hourly_data(timestamp, pollutants):
    # Calculate AQI for each pollutant
    aqi_data = {}
    for pol, value in pollutants.items():
        if value is not None:
            aqi = compute_aqi(value, AQI_BREAKPOINTS.get(pol, []))
            aqi_data[f"aqi_{pol}"] = aqi

    total_aqi = max(filter(None, aqi_data.values()))

    # Store in DB
    conn = sqlite3.connect("backend/aircast.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pollutants_aqi (
            timestamp, pm25, pm10, co, o3, no2, so2,
            aqi_pm25, aqi_pm10, aqi_co, aqi_o3, aqi_no2, aqi_so2, total_aqi
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        pollutants.get("pm25"),
        pollutants.get("pm10"),
        pollutants.get("co"),
        pollutants.get("o3"),
        pollutants.get("no2"),
        pollutants.get("so2"),
        aqi_data.get("aqi_pm25"),
        aqi_data.get("aqi_pm10"),
        aqi_data.get("aqi_co"),
        aqi_data.get("aqi_o3"),
        aqi_data.get("aqi_no2"),
        aqi_data.get("aqi_so2"),
        total_aqi
    ))

    conn.commit()
    conn.close()
    print(f"Stored AQI data for {timestamp}")

### SAMPLE DATA BELOW ###

def insert_sample_data():
    from datetime import datetime
    samples = [
        ("2025-07-28 06:00", {"pm25": 55, "pm10": 100, "co": 7.1, "o3": 0.068, "no2": 120, "so2": 45}),
        ("2025-07-28 07:00", {"pm25": 35, "pm10": 70, "co": 6.5, "o3": 0.058, "no2": 80, "so2": 30}),
        ("2025-07-28 08:00", {"pm25": 28, "pm10": 65, "co": 5.2, "o3": 0.050, "no2": 65, "so2": 28}),
        ("2025-07-28 09:00", {"pm25": 22, "pm10": 55, "co": 4.8, "o3": 0.045, "no2": 50, "so2": 25}),
        ("2025-07-28 10:00", {"pm25": 48, "pm10": 90, "co": 5.5, "o3": 0.062, "no2": 110, "so2": 38}),
        ("2025-07-28 11:00", {"pm25": 75, "pm10": 120, "co": 7.8, "o3": 0.071, "no2": 160, "so2": 50}),
    ]
    for timestamp, data in samples:
        process_hourly_data(timestamp, data)

if __name__ == "__main__":
    insert_sample_data()
