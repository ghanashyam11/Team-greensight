import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

def create_model():
    model = models.Sequential([
        layers.Conv2D(16, (3,3), activation='relu', input_shape=(32,32,1)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(32, (3,3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    X = np.random.rand(200, 32, 32, 1)
    y = np.random.randint(0, 2, 200)
    model = create_model()
    model.fit(X, y, epochs=5, batch_size=8, verbose=1)
    model.save("backend/model/vegetation_cnn.h5")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()
