from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = [float(request.form.get(col)) for col in [
            "Pregnancies", "Glucose", "BloodPressure", "Insulin", "BMI", "Age"
        ]]
        prediction = model.predict([data])[0]
        result = "will develop gestational diabetes" if prediction == 1 else "will not develop gestational diabetes"
        return render_template("index.html", prediction_text=f"The model predicts that the person {result}.")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

# Optional: API endpoint
@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    features = [data[col] for col in ["Pregnancies", "Glucose", "BloodPressure", "Insulin", "BMI", "Age"]]
    prediction = model.predict([features])[0]
    return jsonify({
        "prediction": int(prediction),
        "result": "gestational diabetes" if prediction == 1 else "no gestational diabetes"
    })

if __name__ == "__main__":
    app.run(debug=True)