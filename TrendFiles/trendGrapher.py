import matplotlib.pyplot as plt
import json
from os import mkdir

with open("modelPredictions.json") as f:
    data = json.load(f)

with open("inputData.json") as f:
    inputData = json.load(f)

types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
for model_type in types:
    try:
        mkdir(f"Graphs\\{model_type}")
    except:
        pass
    temp_types = ["BPM", "Concentration", "Exercise", "Gaming", "Happiness", "Sleep", "Stress", "Tiredness"]
    temp_types.remove(model_type)
    for category in temp_types:
        y = data[f"{model_type}-{category}"]
        plt.ylabel(model_type)
        ax = plt.gca()
        if model_type == "BPM":
            ax.set_ylim([0, 150])
        else:
            ax.set_ylim([0, 10])

        if category == "BPM":
            x = inputData["BPM"]
            plt.xlabel("BPM")
            ax.set_xlim([0, 150])
        else:
            x = inputData["General"]
            plt.xlabel(category)
            ax.set_xlim([0, 10])
        
        plt.plot(x, y, marker="o")
        plt.savefig(f"Graphs\\{model_type}\\{category}.png")
        plt.clf()

