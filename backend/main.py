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
    conn = sqlite3.connect("aircast.db")
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
    #PLEASE INSERT DATA INTO HERE
    #Either LIVE API KEY FOR DATA COLLECTION
    #OR sample data

    ]
    for timestamp, data in samples:
        process_hourly_data(timestamp, data)

if __name__ == "__main__":
    insert_sample_data()
