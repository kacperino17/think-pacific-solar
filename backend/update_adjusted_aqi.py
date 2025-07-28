# update_adjusted_all.py

from weather import apply_weather_modifier
import sqlite3

weather_data = {
    "2025-07-28 06:00": {"wind_speed": 0.5, "humidity": 85, "rainfall": 0, "pressure": 1022},
    "2025-07-28 07:00": {"wind_speed": 3.2, "humidity": 60, "rainfall": 1.0, "pressure": 1010},
    "2025-07-28 08:00": {"wind_speed": 6.1, "humidity": 75, "rainfall": 0, "pressure": 1025},
    "2025-07-28 09:00": {"wind_speed": 1.2, "humidity": 88, "rainfall": 0.5, "pressure": 1028},
    "2025-07-28 10:00": {"wind_speed": 4.5, "humidity": 70, "rainfall": 0, "pressure": 1015},
    "2025-07-28 11:00": {"wind_speed": 0.9, "humidity": 90, "rainfall": 0, "pressure": 1030},
}

def apply_modifiers():
    conn = sqlite3.connect("backend/aircast.db")
    cursor = conn.cursor()

    for timestamp, weather in weather_data.items():
        cursor.execute("SELECT total_aqi FROM pollutants_aqi WHERE timestamp = ?", (timestamp,))
        result = cursor.fetchone()
        if result:
            original_aqi = result[0]
            adjusted_aqi = apply_weather_modifier(original_aqi, **weather)

            cursor.execute("""
                INSERT INTO month_01_database (
                    timestamp, original_aqi, adjusted_aqi, wind_speed, humidity, rainfall, pressure
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                timestamp, original_aqi, adjusted_aqi,
                weather["wind_speed"], weather["humidity"],
                weather["rainfall"], weather["pressure"]
            ))
            print(f"{timestamp} → Original AQI: {original_aqi} → Adjusted AQI: {adjusted_aqi}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    apply_modifiers()
