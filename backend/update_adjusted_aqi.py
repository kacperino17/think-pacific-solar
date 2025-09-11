# update_adjusted_all.py

from weather import apply_weather_modifier
import sqlite3

weather_data = {
    #PLEASE INSERT DATA INTO HERE
    #Either LIVE API KEY FOR DATA COLLECTION
    #OR sample data
}

def apply_modifiers():
    conn = sqlite3.connect("aircast.db")
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
