import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_species = None
    if request.method == "POST":
        try:
            # Get the input data from the form
            sepal_length = float(request.form["feature0"])
            sepal_width = float(request.form["feature1"])
            petal_length = float(request.form["feature2"])
            petal_width = float(request.form["feature3"])

            # Predict the class (species) as an integer
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
            print(f"Model Prediction (Integer): {prediction}")  # Add print statement

            # Map the prediction (integer) to the species name
            iris_classes = ["Setosa", "Versicolor", "Virginica"]
            predicted_species = iris_classes[int(prediction)]  # Convert integer to species name

        except Exception as e:
            predicted_species = f"Error: {str(e)}"

    return render_template("index.html", predicted_species=predicted_species)

if __name__ == "__main__":
    app.run(debug=True)
