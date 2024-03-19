import serial
import json
import matplotlib.pyplot as plt
from improvementPredictor import predictImprovement

ser = serial.Serial(port="COM5", baudrate=115200)

message = None
while not message:
    message = str(ser.readline().decode("UTF-8"))[1:].replace("'", "")

print(message)
goals = message.split(";")
with open("progress.json") as f:
    data = json.load(f)

data["Goal1"].append(float(goals[0]))
data["Goal2"].append(float(goals[1]))


attr1, improv1 = predictImprovement()
attr2, improv2 = predictImprovement()
data["Attribute1"].append(attr1)
data["Attribute2"].append(attr2)

with open("progress.json", "w") as f:
    json.dump(data, f)

# graphs
inputdata = list(range(len(data["Attribute1"])))
plt.plot(inputdata, data["Attribute1"], label="Attribute Progress")
plt.plot(inputdata, data["Goal1"], label="Goal Progress")

plt.title("Attribute1 and goal1 progress")
plt.legend()
plt.savefig("ProgressGraphs\Attr+Goal_1.png")
plt.show()
plt.clf()

plt.plot(inputdata, data["Attribute2"], label="Attribute Progress")
plt.plot(inputdata, data["Goal2"], label="Goal Progress")

plt.title("Attribute2 and goal2 progress")
plt.legend()
plt.savefig("ProgressGraphs\Attr+Goal_2.png")
plt.show()
plt.clf()