from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Sentiment Prediction API! Use /predict endpoint with POST method."

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get JSON data from request
            data = request.get_json()
            if not data or "text" not in data:
                return jsonify({"error": "Please provide 'text' in JSON format."}), 400

            text = data["text"]

            # Model prediction
            prediction = model.predict([text])

            # Convert prediction to human-readable sentiment
            sentiment = "Positive" if prediction[0] == 1 else "Negative"

            return jsonify({"text": text, "sentiment": sentiment})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return "Send a POST request to this endpoint with a JSON payload containing 'text'."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)