from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model (Make sure flight_delay_model.pkl is in the same folder)
model = joblib.load("flight_delay_model.pkl")

@app.route('/')
def home():
    return "Flight Delay Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(np.array(data["features"]).reshape(1, -1))
    return jsonify({"delay_prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
