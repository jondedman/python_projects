import turtle as t
from turtle import Screen
from random import randint

t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color = random_color()

# timmy.pensize(5)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.speed("fastest")
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.pencolor(random_color())

draw_spirograph(5)


screen = Screen()

screen.exitonclick()
