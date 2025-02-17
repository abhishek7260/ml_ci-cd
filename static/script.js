document.getElementById("predict-form").onsubmit = async function(event) {
    event.preventDefault();

    let formData = new FormData(event.target);

    let response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    let result = await response.json();

    if (result.prediction) {
        document.getElementById("result").innerText = "Predicted Species: " + result.prediction;
    } else {
        document.getElementById("result").innerText = "Error: " + result.error;
    }
};
