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

timmy.pensize(5)






# def triangle():
#     for _ in range(3):
#         timmy.forward(100)
#         timmy.right(120)

# def square():
#     for _ in range(4):
#         timmy.forward(100)
#         timmy.right(90)

# def pentagon():
#     for _ in range(5):
#         timmy.forward(100)
#         timmy.right(72)

# def hexagon():
#     for _ in range(6):
#         timmy.forward(100)
#         timmy.right(60)

# def heptagon():
#     for _ in range(7):
#         timmy.forward(100)
#         timmy.right(51.42)

# def octagon():
#     for _ in range(8):
#         timmy.forward(100)
#         timmy.right(45)

# def nonagon():
#     for _ in range(9):
#         timmy.forward(100)
#         timmy.right(40)

# def decagon():
#     for _ in range(10):
#         timmy.forward(100)
#         timmy.right(36)

# random_color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "brown", "grey"]


# shapes = [triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon]
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

# for shape in shapes:
#     timmy.color(random_color[randint(0, 9)])
#     shape()


for _ in range(100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(randint(0, 360))




screen = Screen()

screen.exitonclick()
