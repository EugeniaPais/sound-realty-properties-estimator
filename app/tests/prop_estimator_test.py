from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["status"] ==  "ok"


def test_predict():
    # Test with valid input
    valid_input = {
        "zipcode": "98118",
        "bedrooms": 4,
        "bathrooms": 1.0,
        "sqft_living": 1680,
        "sqft_lot": 5043,
        "floors": 1.5,
        "sqft_above": 1680,
        "sqft_basement": 0,
        "waterfront": 0,
        "view": 0,
        "condition": 4,
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=valid_input)
        assert response.status_code == 200
        assert "price" in response.json()


def test_invalid_predict():
    # Test with invalid input (invalid zipcode)
    invalid_input = {
        "zipcode": "00000",
        "bedrooms": 4,
        "bathrooms": 1.0,
        "sqft_living": 1680,
        "sqft_lot": 5043,
        "floors": 1.5,
        "sqft_above": 1680,
        "sqft_basement": 0,
        "waterfront": 0,
        "view": 0,
        "condition": 4,
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=invalid_input)
        assert response.status_code == 422
        assert response.json()["detail"] == "The zipcode is invalid."


def test_predict_minimal():
    # Test with valid input
    valid_input = {
        "zipcode": "98118",
        "bedrooms": 4,
        "bathrooms": 1.0,
        "sqft_living": 1680,
        "sqft_lot": 5043,
        "floors": 1.5,
        "sqft_above": 1680,
        "sqft_basement": 0,
    }
    with TestClient(app) as client:
        response = client.post("/predict-minimal", json=valid_input)
        assert response.status_code == 200
        assert "price" in response.json()


def test_invalid_predict_minimal():
    # Test with incomplete input (missing bedrooms)
    invalid_input = {
        "zipcode": "98118",
        "bathrooms": 1.0,
        "sqft_living": 1680,
        "sqft_lot": 5043,
        "floors": 1.5,
        "sqft_above": 1680,
        "sqft_basement": 0,
    }
    with TestClient(app) as client:
        response = client.post("/predict-minimal", json=invalid_input)
        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "Field required"
        assert response.json()["detail"][0]["loc"] == ["body", "bedrooms"]
