# backend/ai/step2_model.py

from statsmodels.tsa.arima.model import ARIMA

def forecast_aqi_arima(series, steps=6):
    model = ARIMA(series, order=(2, 1, 2))  # Adjust as needed
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast
