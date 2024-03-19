# Imports go at the top
from microbit import *
import random

state = 0
uart.init(baudrate=115200)
message = None
send_data = False

messages = [
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible.",
    "Don't wait for opportunity. Create it.",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Believe you can and you're halfway there.",
    "Your attitude determines your direction.",
    "Don't stop until you're proud.",
    "It always seems impossible until it's done.",
    "You are capable of more than you know.",
    "Strive for progress, not perfection.",
    "Don't wish for it. Work for it.",
    "Success is not just about making money. It's about making a difference.",
    "Make today amazing.",
    "You are stronger than you think.",
    "The only way to do great work is to love what you do.",
    "Don't be afraid to give up the good to go for the great.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "You don't have to be great to start, but you have to start to be great.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "In the middle of every difficulty lies opportunity.",
    "The harder you work, the luckier you get.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Set your goals high, and don't stop till you get there.",
    "Make each day your masterpiece.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "Strive for progress, not perfection.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only way to achieve the impossible is to believe it is possible.",
    "The secret of getting ahead is getting started.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
    "Success is not in what you have, but who you are.",
    "Believe you can and you're halfway there.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "You are never too old to set another goal or to dream a new dream.",
    "The secret of getting ahead is getting started.",
    "The only way to do great work is to love what you do.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "You are never too old to set another goal or to dream a new dream.",
    "The secret of getting ahead is getting started.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
    "Success is not in what you have, but who you are.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "Make each day your masterpiece.",
    "Set your goals high, and don't stop till you get there.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "The harder you work, the luckier you get.",
    "In the middle of every difficulty lies opportunity.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don't be afraid to give up the good to go for the great.",
    "You are capable of more than you know.",
    "The only way to do great work is to love what you do.",
    "You are stronger than you think.",
    "Make today amazing.",
    "Success is not just about making money. It's about making a difference.",
    "Don't wish for it. Work for it.",
    "Strive for progress, not perfection.",
    "You are capable of more than you know.",
    "Believe you can and you're halfway there.",
    "Your attitude determines your direction.",
    "Don't stop until you're proud.",
    "It always seems impossible until it's done.",
    "Dream bigger. Do bigger.",
    "Don't wait for opportunity. Create it.",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Success doesn't just find you. You have to go out and get it.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Don't stop when you're tired. Stop when you're done.",
    "Great things never come from comfort zones.",
    "Push yourself, because no one else is going to do it for you.",
    "Your limitation—it's only your imagination.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
]
    
while message == None:
    message = uart.read(3)
message = str(message, "UTF-8")
categories = message.split(";")
display.scroll(str(categories))
goals = [0, 0]
improvementable = ["BPM", "Gaming", "Concentration", "Sleep", "Exercise", "Tiredness", "Stress", "Happiness"]

bA = button_a.was_pressed()
bB = button_b.was_pressed()
bAB = bA and bB
while not send_data:

    if not bAB:
        if bA:
            state += 1
            if state >= 4:
                state = 0
    else:
        send_data = not send_data
    
    if state == 0 or state == 1:
        display.scroll(str(improvementable[int(categories[state])]) + " Goal: " + str(goals[state]), 65)
        if goals[state] > 0:
            display.scroll("Goal Completed; Great Job!!!", 55)
        else:
            display.scroll("You need to finish your goal.", 55)

        if bB:
            goals[state] += 1
            
            
    if state == 2:
        display.scroll(random.choice(messages), 75)
        sleep(5000)

    
    bA = button_a.was_pressed()
    bB = button_b.was_pressed()
    bAB = bA and bB

send_string = str(goals[0])+ ";" + str(goals[1])
while send_data:
    print(send_string.encode('UTF-8'))
    sleep(1000)
    
