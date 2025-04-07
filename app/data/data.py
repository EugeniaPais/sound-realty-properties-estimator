from pathlib import Path
from pandas import read_csv, DataFrame

BASE_DIR = Path(__file__).resolve(strict=True).parent

def load_zip_demographics() -> DataFrame:
    """Load the zip code demographics data."""
    zip_demographics_path = f"{BASE_DIR}/zipcode_demographics.csv"
    zip_demographics = read_csv(zip_demographics_path, dtype={"zipcode": str})
    return zip_demographics