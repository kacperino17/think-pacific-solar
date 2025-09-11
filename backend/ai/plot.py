#plot.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast_matplotlib(actual_df, forecast):
    future_index = pd.date_range(start=actual_df.index[-1] + pd.Timedelta(hours=1), periods=6, freq='H')
    
    plt.figure(figsize=(10, 5))
    plt.plot(actual_df.index, actual_df['adjusted_aqi'], label="Actual AQI", marker='o')
    plt.plot(future_index, forecast, label="Predicted AQI", linestyle='--', marker='x', color='orange')

    plt.xlabel("Time")
    plt.ylabel("AQI")
    plt.title("AQI Forecast (Adjusted)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
