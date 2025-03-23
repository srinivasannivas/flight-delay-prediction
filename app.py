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

dataset1 = st.sidebar.file_uploader("Upload Flight Delay Dataset", type=["csv"])

# Initialize airline options
airline_options = ["Select an Airline"]

# Load dataset
if dataset1:
    try:
        df1 = pd.read_csv(dataset1)
        st.subheader("📊 Flight Data Preview")
        st.dataframe(df1.head())  # Show preview of dataset

        # Check if "Airline" column exists
        if "Airline" in df1.columns:
            airline_options = sorted(df1["Airline"].dropna().unique())  # Extract unique airlines
        else:
            st.sidebar.error("Dataset must contain an 'Airline' column!")

    except Exception as e:
        st.sidebar.error(f"Error loading dataset: {e}")

# User input fields for prediction
st.header("🛫 Enter Flight Details")

# Airline selection
airline = st.selectbox("✈️ Select Airline", airline_options)

# Departure time input
departure_time = st.slider("⏰ Departure Time (24h format)", 0, 23, 12)

# Weather condition input
weather = st.selectbox("🌤️ Weather Condition", ["Clear", "Rainy", "Stormy", "Snowy"])

# Prediction function
def predict_delay(airline, departure_time, weather):
    if weather in ["Stormy", "Snowy"]:
        return "High chance of delay ❌"
    elif departure_time in range(18, 23):
        return "Moderate chance of delay ⚠️"
    else:
        return "Likely to be on time ✅"

# Prediction button
if st.button("🔍 Predict Delay"):
    if airline == "Select an Airline":
        st.warning("Please upload a dataset and select an airline!")
    else:
        prediction = predict_delay(airline, departure_time, weather)
        st.subheader(f"Prediction: {prediction}")

# Debugging output (optional)
st.sidebar.write("Loaded Airlines:", airline_options)
