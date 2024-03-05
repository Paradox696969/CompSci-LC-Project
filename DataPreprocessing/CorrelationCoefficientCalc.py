import matplotlib.pyplot as plt
import pandas as pd
import numpy
import json

df = pd.read_csv("CollectedData.csv")
cols = list(dict(df).keys())
cols = cols[1:]

correlations = {}

for i in cols:
    for j in cols:
        if i != j:
            correlations[f"{i}-{j}"] = numpy.corrcoef(list(df[i]), list(df[j]))[0, 1]

with open("correlations.json", "w") as f:
    json.dump(correlations, f, indent=1)