import matplotlib.pyplot as plt
import json
from os import mkdir

with open("derivativeData.json") as f:
    data = json.load(f)

with open("inputData.json") as f:
    inputData = json.load(f)

types = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
for model_type in types:
    try:
        mkdir(f"DerivativeGraphs\\{model_type}")
    except:
        pass
    temp_types = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
    temp_types.remove(model_type)
    for category in temp_types:
        y = data[f"{model_type}-{category}"]
        plt.ylabel(f"{model_type}/{category}")
        ax = plt.gca()

        if category == "BPM":
            x = inputData["BPM"]
            plt.xlabel("BPM")
        else:
            x = inputData["General"]
            plt.xlabel(category)
        
        plt.plot(x[:len(y)], y, marker="o")
        plt.savefig(f"DerivativeGraphs\\{model_type}\\{category}.png")
        plt.clf()

