import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the trained model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_species = None
    if request.method == "POST":
        try:
            # Get input data from the form
            sepal_length = float(request.form["feature0"])
            sepal_width = float(request.form["feature1"])
            petal_length = float(request.form["feature2"])
            petal_width = float(request.form["feature3"])

            # Predict species
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
            iris_classes = ["Setosa", "Versicolor", "Virginica"]
            predicted_species = iris_classes[int(prediction)]

        except Exception as e:
            predicted_species = f"Error: {str(e)}"

    return render_template("index.html", predicted_species=predicted_species)

@app.route("/predict", methods=["POST"])
def predict():
    """API endpoint for CI/CD testing"""
    data = request.get_json()
    
    if "features" not in data or not isinstance(data["features"], list) or len(data["features"]) != 4:
        return jsonify({"error": "Invalid input format. Expected 4 numerical values."}), 400

    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        species = ["Setosa", "Versicolor", "Virginica"]
        return jsonify({"prediction": species[int(prediction)]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
