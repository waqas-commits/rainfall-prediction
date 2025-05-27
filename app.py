import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('rainfall_model.pkl', 'rb'))

st.title("Rainfall Prediction App")

# User inputs
temp = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
pressure = st.number_input("Pressure (hPa)", min_value=800.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0)

if st.button("Predict"):
    features = np.array([[temp, humidity, pressure, wind_speed]])
    prediction = model.predict(features)
    st.success(f"Predicted Rainfall: {prediction[0]:.2f} mm")