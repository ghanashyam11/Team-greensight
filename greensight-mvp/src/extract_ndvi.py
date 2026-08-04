import rasterio
import matplotlib.pyplot as plt
import numpy as np

def compute_ndvi(image_path):
    with rasterio.open(image_path) as src:
        img = src.read()
        red = img[2].astype(float)
        nir = img[3].astype(float)
        ndvi = (nir - red) / (nir + red + 1e-10)
        return ndvi

def plot_ndvi(ndvi):
    plt.imshow(ndvi, cmap='YlGn')
    plt.title("NDVI Vegetation Map")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    ndvi = compute_ndvi("data/satellite_image.tif")
    plot_ndvi(ndvi)
