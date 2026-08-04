from fastapi import FastAPI
from src.extract_ndvi import compute_ndvi
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GreenSight AI + LiDAR API Running"}

@app.get("/analyze")
def analyze():
    ndvi = compute_ndvi("data/satellite_image.tif")
    avg_health = np.mean(ndvi)
    return {"average_ndvi": float(avg_health)}
