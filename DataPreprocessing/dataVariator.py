import pandas as pd
import random as random

df = pd.read_csv("CollectedData.csv").to_dict(orient="list")
varied_data = pd.read_csv("CollectedData.csv").to_dict(orient="list")
for i in range(1000):
    for key in df.keys():
        for item in df[key]:
            varied_data[key].append(round(item + random.random()*random.choice([1, -1])*0.5, 4))
        

pd.DataFrame(varied_data).to_csv(".\COMPSCI-Project\VariedData.csv", index=False)

