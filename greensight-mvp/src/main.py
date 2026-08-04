from preprocess_lidar import load_lidar, compute_canopy_metrics
from extract_ndvi import compute_ndvi
from vegetation_model import create_model
import numpy as np


def run_pipeline():
    print("🌿 GreenSight MVP Pipeline Start")

    # Step 1: LiDAR
    pts = load_lidar("data/forest_sample.las")
    h, d = compute_canopy_metrics(pts)
    print(f"[LiDAR] Canopy Height: {h:.2f} | Density: {d:.4f}")

    # Step 2: NDVI
    ndvi = compute_ndvi("data/satellite_image.tif")
    print(f"[NDVI] NDVI Range: {ndvi.min():.2f} - {ndvi.max():.2f}")

    # Step 3: AI model (simulation)
    model = create_model()
    test_input = np.random.rand(1, 32, 32, 1)
    pred = model.predict(test_input)
    print(f"[AI] Simulated vegetation health: {'Healthy' if pred[0][1] > 0.5 else 'Stressed'}")

    print("✅ GreenSight MVP Pipeline Completed")


if __name__ == "__main__":
    run_pipeline()
