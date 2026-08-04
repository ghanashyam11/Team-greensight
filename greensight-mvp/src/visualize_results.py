import matplotlib.pyplot as plt
import numpy as np

def simulate_visualization(ndvi):
    health_map = np.where(ndvi > 0.3, "Healthy", "Stressed")
    plt.imshow(ndvi, cmap="YlGn")
    plt.title("Vegetation Health Classification Overlay")
    plt.show()

if __name__ == "__main__":
    ndvi = np.random.rand(100, 100)
    simulate_visualization(ndvi)
