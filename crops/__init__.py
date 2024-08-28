from typing import List
from dataclasses import dataclass

@dataclass
class CropData:
    crop_name: str
    temperature: List[float]
    humidity: List[float]
    soil_moisture: List[float]
    risk_prediction: List[str]