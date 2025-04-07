import pickle
import json
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

def load_model():
    """Load the pre-trained model from the specified path."""
    model_path = f"{BASE_DIR}/prop_estimator_model-{__version__}.pkl"
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def load_features():
    """Load the features used in the model."""
    features_path = f"{BASE_DIR}/prop_estimator_features-{__version__}.json"
    with open(features_path, "r") as f:
        features = json.load(f)
    return features