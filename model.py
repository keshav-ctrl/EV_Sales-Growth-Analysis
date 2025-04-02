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
df.to_csv('ev_data.csv', index=False)