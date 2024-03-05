import serial
from futureImprovementPredictor import predictImprovement

ser = serial.Serial(port="COM5", baudrate=115200)

best, _, _, _ = predictImprovement()
send_string = ""
improvementable = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
for i in range(2):
    send_string += f"{improvementable.index(best[i])};"
send_string = send_string[:-1]
send_string += "\n"
print(send_string)
for i in range(1000):
    ser.write(send_string.encode("UTF-8"))


