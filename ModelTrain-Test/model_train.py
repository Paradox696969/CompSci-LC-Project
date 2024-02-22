import tensorflow as tf
import pandas as pd
import numpy as np

df = pd.read_csv("VariedData.csv")

datasets = {}
for name in list(df.columns.values):
    datasets[name] = [0, 0]
    datasets[name][0] = df.copy()
    datasets[name][1] = datasets[name][0].pop(name)
    datasets[name][0] = np.array(datasets[name][0])
    print(datasets[name])

for dataset in datasets.keys():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(7, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1),
    ])

    model.compile(loss="mse", optimizer="adam")

    model.fit(datasets[dataset][0], datasets[dataset][1], validation_split=0.2, epochs=100)
    model.save(f"Models\\{dataset}.h5")
