import json


def predictImprovement():
    currentstats = [0, 0, 0, 0, 0, 0, 0, 0]
    currentstats[0] = int(input("Measure your current BPM or heart rate and type it out: ")) - 60
    currentstats[1] = float(input("On a scale of 0 to 10, where 0 is not at all and 10 is multiple hours per day, how much time do you spend playing games or using social media?: "))
    currentstats[2] = float(input("Ask someone, on a scale of 0 to 10, where 0 is unfocused and 10 is obsessively focused, how concentrated are you on the important things in you life(school, work, hobbies etc.)?: "))
    currentstats[3] = float(input("How many hours a night are you asleep, where 0 is none and 10 is 10+ hours of sleep?: "))
    currentstats[4] = float(input("How much do you exercise on average per day where 0 is a highly sedentary and inactive lifestyle and 10 is competitive sports/athletics amount?: "))
    currentstats[5] = float(input("How tired are you on average throughout a day where 0 is at risk of falling asleep at any moment and 10 is hyperactive or overly energetic?: "))
    currentstats[6] = float(input("How stressed are you on a daily basis where 0 is not stressed at all and 10 is on the verge of mental collapse?: "))
    currentstats[7] = float(input("How happy or mentally healthy are you on a daily basis, where 0 is very depressed(seek help please) and 10 is you're at the prime of your life and incredibly happy?: "))


    iterations = 16000
    dx = [10/iterations, (0.5*160)/iterations]
    improvementable = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
    wantedImprovement = improvementable.index(input(f"what do you want to improve from the following list:\n\n{improvementable}\n\nAnswer: "))
    improvementable_copy = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
    improvementable_copy.pop(wantedImprovement)

    with open("derivativeData.json") as f:
        derivativeData = json.load(f)

    increase = [0, 0, 1, 1, 1, 1, 0, 1]
    derivatives = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(currentstats)):
        if i != wantedImprovement:
            if i != 0:
                derivatives[i] = derivativeData[f"{improvementable[wantedImprovement]}-{improvementable[i]}"][int(currentstats[i]/dx[0])]
            else:
                derivatives[i] = derivativeData[f"{improvementable[wantedImprovement]}-{improvementable[i]}"][int(currentstats[i]/dx[1])]

        else:
            derivatives[i] = "a"
    derivatives.remove("a")
    derivatives_copy = derivatives.copy()
    best = []
    best_values = []
    worst = []
    worst_values = []
    for i in range(2):
        if increase[wantedImprovement]:
            max_d = max(derivatives)
            best_values.append(max_d)
            best.append(improvementable_copy[derivatives_copy.index(max_d)])
            derivatives.remove(max_d)
            min_d = min(derivatives)
            worst_values.append(min_d)
            worst.append(improvementable_copy[derivatives_copy.index(min_d)])
            derivatives.remove(min_d)
        else:
            max_d = max(derivatives)
            worst_values.append(max_d)
            worst.append(improvementable_copy[derivatives_copy.index(max_d)])
            derivatives.remove(max_d)
            min_d = min(derivatives)
            best_values.append(min_d)
            best.append(improvementable_copy[derivatives_copy.index(min_d)])
            derivatives.remove(min_d)
    
    return best, best_values, worst, worst_values

if __name__ == "__main__":
    best, best_values, worst, worst_values = predictImprovement()
    print(f"BestDerivativeData: {best_values}")
    print(f"WorstDerivativeData: {worst_values}")
    print(f"You should aim to improve your {best[0]} and do some work on your {best[1]}.")
    print(f"You should also aim to lessen your {worst[0]} and do some work on your {worst[1]}.")