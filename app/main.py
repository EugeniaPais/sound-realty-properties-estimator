from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pandas import DataFrame
from pydantic import BaseModel
from app.services import PropEstimatorInput, PropEstimatorOutput, PropEstimatorFullInput
from app.models.prop_estimator_model import load_model, load_features, __version__
from app.data.data import load_zip_demographics


ml_models = {}


def _prepare_input(input: BaseModel):
    data = input.model_dump()
    input_df = DataFrame([data])

    # Check if the zip_code exists in the demographics data
    if (
        input_df["zipcode"].iloc[0]
        not in ml_models["zip_demographics"]["zipcode"].values
    ):
        raise ValueError("The zipcode is invalid.")

    merged_data = input_df.merge(
        ml_models["zip_demographics"], how="left", on="zipcode"
    ).drop(columns="zipcode")
    return merged_data[ml_models["features"]]


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models["model"] = load_model()
    ml_models["features"] = load_features()
    ml_models["zip_demographics"] = load_zip_demographics()
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(
    lifespan=lifespan,
    title="Property Price Estimator",
    description="API for estimating property prices based on various features.",
)


@app.get("/")
async def root():
    """Root endpoint to check if the API is running."""
    return {"status": "ok", "model_version": __version__}


@app.post("/predict")
def predict(input: PropEstimatorFullInput):
    """
    Endpoint to predict property prices based on the input features.
    Args:
        input (PropEstimatorFullInput): Input data for property price estimation,
        including the whole set of features.
    Returns:
        PropEstimatorOutput: Predicted property price.
    """
    try:
        model = ml_models["model"]
        prediction = model.predict(_prepare_input(input))
        return PropEstimatorOutput(price=prediction[0])
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occurred.")


@app.post("/predict-minimal")
def predict_basic(input: PropEstimatorInput):
    """Endpoint to predict property prices based on the minimal set of input features.
    Args:
        input (PropEstimatorInput): Input data for property price estimation,
        including only the minimal features.
    Returns:
        PropEstimatorOutput: Predicted property price.
    """
    # Check if the input is valid
    try:
        model = ml_models["model"]
        prediction = model.predict(_prepare_input(input))
        return PropEstimatorOutput(price=prediction[0])
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occurred.")
