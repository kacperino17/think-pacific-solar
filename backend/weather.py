# weather.py

def apply_weather_modifier(aqi, wind_speed, humidity, rainfall, pressure):
    modified_aqi = aqi

    # Wind speed rule
    if wind_speed < 1.5:
        modified_aqi *= 1.1
    elif wind_speed > 5:
        modified_aqi *= 0.9

    # Humidity (optional)
    if humidity > 80:
        modified_aqi *= 1.05

    # Rainfall
    if rainfall > 0:
        modified_aqi *= 0.8

    # Pressure/inversions (example logic)
    if pressure > 1020:
        modified_aqi *= 1.2

    return round(modified_aqi, 2)
