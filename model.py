# Data Collection and processing
import pandas as pd
import numpy as np

# Synthetic Data (Replace with real datasets)
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'EV_Sales': [0.5, 0.8, 1.2, 2.0, 2.8, 3.5, 5.0, 7.5, 10.0],  # In millions
    'Battery_Cost': [350, 300, 250, 200, 180, 150, 130, 110, 100],  # $/kWh
    'Charging_Stations': [100, 150, 300, 500, 800, 1200, 1800, 2500, 3500]
}

df = pd.DataFrame(data)
df.to_csv('ev_data1.csv', index=False)


# EDA
import matplotlib.pyplot as plt
import seaborn as sns

# Plot EV Sales Growth
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='EV_Sales', data=df, marker='o')
plt.title('Global EV Sales Growth (2015-2023)')
plt.ylabel('Sales (Millions)')
plt.show()

# Correlation Matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# forecasiting  using prophet
from prophet import Prophet

# Prepare data for Prophet
forecast_df = df[['Year', 'EV_Sales']].rename(columns={'Year': 'ds', 'EV_Sales': 'y'})
forecast_df['ds'] = pd.to_datetime(forecast_df['ds'], format='%Y')

# Train model
model = Prophet(yearly_seasonality=True)
model.fit(forecast_df)

# Predict next 5 years
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

# Plot forecast
fig = model.plot(forecast)
plt.title('EV Sales Forecast (Prophet Model)')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.show()