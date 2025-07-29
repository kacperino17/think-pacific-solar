# backend/view_interface.py

import streamlit as st
import sqlite3
import pandas as pd
from datetime import timedelta

# === Import AI modules ===
from ai.data import get_adjusted_aqi_series
from ai.model_arima import forecast_aqi_arima


st.set_page_config(page_title="AirCast Dashboard", layout="wide")

# === Helper: Table Fetch ===
def fetch_table(name):
    conn = sqlite3.connect("aircast.db")
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)
    conn.close()
    return df

# === Section 1: Table Viewer ===
st.title("📋 AirCast Data Viewer")

with st.expander("🔍 View Raw Data Tables"):
    table = st.selectbox("Select Table to View", ["pollutants_aqi", "month_01_database"])
    df_table = fetch_table(table)
    st.dataframe(df_table)

# === Section 2: AQI Forecasting ===
st.header("📈 AQI Forecast (Adjusted for Solar Planning)")

# Load adjusted AQI time series
df = get_adjusted_aqi_series()
last_6_actual = df.tail(6)
forecast = forecast_aqi_arima(last_6_actual['adjusted_aqi'])

# Create future timestamps
future_index = pd.date_range(start=last_6_actual.index[-1] + timedelta(hours=1), periods=6, freq='H')
predicted_df = pd.DataFrame({'Predicted AQI': forecast}, index=future_index)

# Combine for chart
combined_df = pd.concat([
    last_6_actual[['adjusted_aqi']].rename(columns={"adjusted_aqi": "Actual AQI"}),
    predicted_df
], axis=0)

# Plot
st.line_chart(combined_df)

# Recommendations
def aqi_to_recommendation(aqi):
    if aqi < 50:
        return "✅ Excellent solar efficiency."
    elif aqi < 100:
        return "🟡 Good, minor impact expected."
    elif aqi < 150:
        return "🟠 Moderate air quality – monitor panel output."
    else:
        return "🔴 Poor air quality – expect reduced efficiency."

st.subheader("Solar Efficiency Forecast")
for ts, val in predicted_df['Predicted AQI'].items():
    st.markdown(f"**{ts.strftime('%Y-%m-%d %H:%M')}** — AQI: `{int(val)}` → {aqi_to_recommendation(val)}")
