import pandas as pd
import numpy as np

# Generate 10,000 random flight records
num_samples = 10000

data = {
    "Flight_ID": np.arange(1, num_samples + 1),  # Unique flight numbers
    "Airline": np.random.choice(["Delta", "United", "American", "Southwest", "JetBlue"], num_samples),
    "Origin_Airport": np.random.choice(["JFK", "LAX", "ORD", "ATL", "DFW"], num_samples),
    "Destination_Airport": np.random.choice(["MIA", "SEA", "DEN", "BOS", "PHX"], num_samples),
    "Scheduled_Departure": np.random.randint(0, 24, num_samples),  # Hour of departure
    "Weather_Delay": np.random.randint(0, 60, num_samples),  # Delay due to weather in minutes
    "Air_Traffic_Delay": np.random.randint(0, 60, num_samples),  # Delay due to traffic
    "Security_Delay": np.random.randint(0, 15, num_samples),  # Delay due to security checks
    "Aircraft_Maintenance_Delay": np.random.randint(0, 30, num_samples),  # Delay due to maintenance
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total delay (sum of all delay factors)
df["Total_Delay"] = df["Weather_Delay"] + df["Air_Traffic_Delay"] + df["Security_Delay"] + df["Aircraft_Maintenance_Delay"]

# Save dataset as CSV
df.to_csv("flight_delay.csv", index=False)

print("✅ Sample dataset 'flight_delay.csv' created successfully!")
