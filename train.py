import pandas as pd
import numpy as np
import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("flight_delay.csv")

# Define features (X) and target (y)
X = df.drop(columns=["Total_Delay", "Flight_ID", "Airline", "Origin_Airport", "Destination_Airport"])  # Drop unnecessary columns
y = df["Total_Delay"]

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the XGBoost model
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
print("Root Mean Squared Error (RMSE):", np.sqrt(mean_squared_error(y_test, y_pred)))

# Save the trained model
joblib.dump(model, "flight_delay_model.pkl")
print("✅ Model saved successfully as 'flight_delay_model.pkl'")
