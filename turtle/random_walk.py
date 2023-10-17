import turtle as t
from turtle import Screen
from random import randint

t.colormode(255)

screen = Screen()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple


timmy = t.Turtle()
timmy.shape("turtle")
timmy.color = random_color()

timmy.pensize(5)

for _ in range(100):
    timmy.forward(30)
    timmy.right(randint(0, 360))
    timmy.pencolor(random_color())


screen.exitonclick()
