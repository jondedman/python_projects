from turtle import Turtle, Screen
from random import randint

names = ["tim", "tom", "tam", "tem", "tum", "tym"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400) # width and height of the screen
user_bet = screen.textinput(title="place your bet", prompt="Which color turtle do you want to bet on?")


turtles = []

for i in range(6):
    names[i] = Turtle(shape="turtle")
    names[i].color(colors[i])
    names[i].penup()
    names[i].goto(x=-230, y=-100 + (i * 30))
    turtles.append(names[i])





if user_bet:
    race_on = True

    while race_on:
        rand_distance = randint(0, 30)  # random distance
        for turtle in turtles:
            turtle.forward(rand_distance)
            if turtle.xcor() >= 230:
                race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    screen.title(f"You've won! The {winner} turtle is the winner!")
                else:
                    screen.title(f"You've lost! The {winner} turtle is the winner!")




screen.exitonclick()
