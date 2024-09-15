from turtle import Turtle,Screen
import random

sc = Screen()
race_is_on = False
sc.setup(width=800,height=550)

user_bet = sc.textinput(title="What is Going to be Win",prompt="Enter Color of Your Turtle")
colors = ["red","green","blue","purple","yellow"]
y_index = [-150,-50,50,150,250]

all_turtle = []

for tur_index in range(0,5):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[tur_index])
    new_turtle.goto(x=-370,y=y_index[tur_index])
    all_turtle.append(new_turtle)


if user_bet:
    race_is_on = True

while race_is_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 380:
            race_is_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"Your Win Bro: {wining_color} This Wins Your Turtle is Done:")
            else: 
                print(f"Your loos Bro: {wining_color} This Wins Your Turtle is Done:")
        rand_move = random.randint(0,  10)
        turtle.forward(rand_move)


sc.exitonclick()