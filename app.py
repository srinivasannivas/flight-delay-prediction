from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("flight_delay_model.pkl")

@app.route("/")
def home():
    return "Flight Delay Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the request
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({"predicted_delay": float(prediction)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
