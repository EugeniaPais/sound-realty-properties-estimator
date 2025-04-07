from pydantic import BaseModel, Field
from typing import Optional, Literal


class PropEstimatorInput(BaseModel):
    bedrooms: int = Field(ge=0)
    bathrooms: float = Field(ge=0)
    sqft_living: int = Field(ge=0)
    sqft_lot: int = Field(ge=0)
    floors: float = Field(ge=0)
    sqft_above: int = Field(ge=0)
    sqft_basement: int = Field(ge=0)
    zipcode: str = Field(pattern=r"^\d{5}(-\d{4})?$")


class PropEstimatorFullInput(PropEstimatorInput):
    waterfront: Optional[Literal[0, 1]] = None
    view: Optional[int] = Field(None, ge=0)
    condition: Optional[int] = Field(None, ge=0)
    grade: Optional[int] = Field(None, ge=0)
    year_built: Optional[int] = Field(None, ge=0)
    year_renovated: Optional[int] = Field(None, ge=0)
    lat: Optional[float] = Field(None, ge=-90, le=90)
    long: Optional[float] = Field(None, ge=-180, le=180)
    sqft_living15: Optional[int] = Field(None, ge=0)
    sqft_lot15: Optional[int] = Field(None, ge=0)
