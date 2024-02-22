import tensorflow as tf
import numpy as np
import json

predictions = {}
inputData = {}
iterations = 16000
types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
for model_type in types:
    model = tf.keras.models.load_model(f"Models\\{model_type}.h5")
    data = []
    temp_types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
    temp_types.remove(model_type)
    for i in range(iterations):
        data.append([])
    for category in temp_types:
        for i in range(iterations):
            data[i] = [5, 5, 5, 5, 5, 5, 5]
            if category == "BPM":
                data[i][temp_types.index(category)] = 60+i*((0.5*160)/iterations)
            else:
                data[i][temp_types.index(category)] = i*(10/iterations)


        predictions[f"{model_type}-{category}"] = model.predict(data).flatten().tolist()

inputData["BPM"] = []
inputData["General"] = []
for i in range(iterations):
    inputData["BPM"].append(60+i*((0.5*160)/iterations))
    inputData["General"].append(i*(10/iterations))

with open("modelPredictions.json", "w") as f:
    json.dump(predictions, f, indent=1)

with open("inputData.json", "w") as f:
    json.dump(inputData, f, indent=1)
