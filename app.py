# dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('EV Market Growth Analysis Dashboard')

# Load data
df = pd.read_csv('ev_data.csv')

# Show raw data
st.subheader('Raw Data')
st.write(df)

# Plot EV Sales
st.subheader('EV Sales Over Time')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Year'], df['EV_Sales'], marker='o')
st.pyplot(fig)