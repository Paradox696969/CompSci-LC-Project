import tensorflow as tf
import numpy as np

model_type = input("What model?: ")

#79, 10, 3, 8, 3, 8, 3, 8
data = np.array([[79, 10, 3, 8, 3, 8, 8]])
model = tf.keras.models.load_model(f"Models\\{model_type}.h5")
print(model.predict(data))