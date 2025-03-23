import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide",
)

# Title and description
st.title("✈️ Flight Delay Prediction App")
st.markdown(
    """
    Welcome to the **Flight Delay Prediction App**!  
    This tool helps predict whether your flight might be delayed based on key factors like airline, departure time, and weather conditions.
    """
)

# Sidebar for dataset upload
st.sidebar.header("📂 Upload Datasets")

dataset1 = st.sidebar.file_uploader("FlightDelayPrediction1.csv", type=["csv"])
dataset2 = st.sidebar.file_uploader("FlightDelayPrediction2.csv", type=["csv"])

# Load dataset and extract airline names
airline_options = ["Select a dataset first"]
if dataset1:
    df1 = pd.read_csv(dataset1)
    if "Airline" in df1.columns:  # Check if the "Airline" column exists
        airline_options = sorted(df1["Airline"].dropna().unique())  # Get unique airline names
    else:
        st.sidebar.error("Dataset must contain an 'Airline' column!")

# Display dataset previews
if dataset1:
    st.subheader("📊 Flight Data Preview")
    st.dataframe(df1.head())

if dataset2:
    st.subheader("📊 Additional Data Preview")
    df2 = pd.read_csv(dataset2)
    st.dataframe(df2.head())

# User input fields for prediction
st.header("🛫 Enter Flight Details")

# Airline selection from dataset
airline = st.selectbox("✈️ Select Airline", airline_options)

departure_time = st.slider("⏰ Departure Time (24h format)", 0, 23, 12)
weather = st.selectbox("🌤️ Weather Condition", ["Clear", "Rainy", "Stormy", "Snowy"])

# Placeholder prediction logic
def predict_delay(airline, departure_time, weather):
    if weather in ["Stormy", "Snowy"]:
        return "High chance of delay ❌"
    elif departure_time in range(18, 23):
        return "Moderate chance of delay ⚠️"
    else:
        return "Likely to be on time ✅"

# Prediction button
if st.button("🔍 Predict Delay"):
    if airline == "Select a dataset first":
        st.warning("Please upload a dataset with an 'Airline' column first!")
    else:
        prediction = predict_delay(airline, departure_time, weather)
        st.subheader(f"Prediction: {prediction}")

