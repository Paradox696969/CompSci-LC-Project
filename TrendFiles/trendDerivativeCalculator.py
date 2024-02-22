import json

with open("modelPredictions.json") as f:
    predictions = json.load(f)

derivativeData = {}
iterations = 16000
dx = [10/iterations, (0.5*160)/iterations]
types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
for model_type in types:
    temp_types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
    temp_types.remove(model_type)
    for category in temp_types:
        data = []
        for i in range(iterations):
            if i < iterations-1:
                dy = predictions[f"{model_type}-{category}"][i+1]-predictions[f"{model_type}-{category}"][i]
                data.append(dy/dx[int(category == "BPM")])
        
        derivativeData[f"{model_type}-{category}"] = data

with open("derivativeData.json", "w") as f:
    json.dump(derivativeData, f, indent=1)