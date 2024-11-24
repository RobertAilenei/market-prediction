import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data
from utils.plot_utils import plot_gold_prices

# Load data
data = load_data('data/gold_prices.csv')

# Streamlit Application
st.title("Gold Price Fluctuation Prediction (Statistical)")

# Sidebar Input
st.sidebar.header("User Input")
days_ahead = st.sidebar.slider("Days ahead to predict", 1, 30, 7)

# Display raw data
st.subheader("Gold Price Data")
st.write(data)

# Plot gold prices
st.subheader("Gold Prices Over Time")
fig = plot_gold_prices(data)
st.pyplot(fig)

# Predict future prices using a simple trend-based approach
st.subheader(f"Prediction for {days_ahead} days ahead")

# Calculate the average daily change
data['Day'] = (data['Date'] - data['Date'].min()).dt.days
data['Daily Change'] = data['Price'].diff()

# Use the mean of recent daily changes to predict
recent_change = data['Daily Change'].mean()
last_price = data['Price'].iloc[-1]
predicted_price = last_price + recent_change * days_ahead

# Display prediction
st.write(f"Predicted Gold Price after {days_ahead} days: {predicted_price:.2f} RON")
st.write("Note: This prediction is based on the average daily change.")
