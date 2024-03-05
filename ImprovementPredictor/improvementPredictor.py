import tensorflow as tf

def predictImprovement():
    currentstats = [0, 0, 0, 0, 0, 0, 0]
    questions = {
        "BPM": "Measure your current BPM or heart rate and type it out: ",
        "Gaming": "On a scale of 0 to 10, where 0 is not at all and 10 is multiple hours per day, how much time do you spend playing games or using social media?: ",
        "Concentration": "Ask someone, on a scale of 0 to 10, where 0 is unfocused and 10 is obsessively focused, how concentrated are you on the important things in you life(school, work, hobbies etc.)?: ",
        "Sleep": "How many hours a night are you asleep, where 0 is none and 10 is 10+ hours of sleep?: ",
        "Exercise": "How much do you exercise on average per day where 0 is a highly sedentary and inactive lifestyle and 10 is competitive sports/athletics amount?: ",
        "Tiredness": "How tired are you on average throughout a day where 0 is at risk of falling asleep at any moment and 10 is hyperactive or overly energetic?: ",
        "Stress": "How stressed are you on a daily basis where 0 is not stressed at all and 10 is on the verge of mental collapse?: ",
        "Happiness": "How happy or mentally healthy are you on a daily basis, where 0 is very depressed(seek help please) and 10 is you're at the prime of your life and incredibly happy?: "
    }

    improvementable = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
    questionable = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]
    
    wantedImprovement = improvementable.index(input(f"what do you want to predict from the following list:\n\n{improvementable}\n\nAnswer: "))
    questionable.pop(wantedImprovement)

    for i in range(len(questionable)):
        currentstats[i] = float(input(questions[questionable[i]]))
    
    model = tf.keras.models.load_model(f"Models\\{improvementable[wantedImprovement]}.h5")
    prediction = model.predict([currentstats]).flatten().tolist()[0]
    
    return prediction, improvementable[wantedImprovement]

def compareImprovement():
    initial, improvement = predictImprovement()
    improved, improvement = predictImprovement()

    print(f"Comparison for {improvement}")
    diff = improved - initial
    print(f"Initial prediction: {round(initial, 3)}\nFinal prediction: {round(improved, 3)}\nEffect: {round(diff, 3)}")

compareImprovement()
    