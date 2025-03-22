import streamlit as st

st.title("Flight Delay Prediction App")
st.write("Welcome! This app will help you predict flight delays.")

# Add input fields
airline = st.selectbox("Select Airline", ["Airline A", "Airline B", "Airline C"])
departure_time = st.slider("Departure Time (24h format)", 0, 23, 12)
weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Stormy", "Snowy"])

# Placeholder for prediction (replace with actual model later)
if st.button("Predict Delay"):
    st.write(f"Prediction: Flight with {airline} at {departure_time}:00 is likely to be on time.")