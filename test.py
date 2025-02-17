import pytest
import json
import pickle
import numpy as np
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_model_loading():
    """Test if the model loads correctly"""
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        assert model is not None
    except Exception as e:
        pytest.fail(f"Model loading failed: {str(e)}")

def test_predict_valid_input(client):
    """Test API with valid input"""
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    data = response.get_json()
    assert response.status_code == 200
    assert "prediction" in data

def test_predict_invalid_input(client):
    """Test API with invalid input"""
    response = client.post("/predict", json={"features": []})
    assert response.status_code == 400

def test_predict_wrong_format(client):
    """Test API with incorrect input format"""
    response = client.post("/predict", json={"wrong_key": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 400
