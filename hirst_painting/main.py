# import colorgram
import turtle as t
from turtle import Screen
import random




# colors = colorgram.extract('hirst_painting/severed-spots.jpg', 30)

# colors_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     colors_list.append((r, g, b))

rgb_colors =[(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]

timmy = t.Turtle()
screen = Screen()

t.colormode(255)


timmy.shape("turtle")
# timmy.color = rgb_colors[randint(0, len(rgb_colors) - 1)]
# timmy.pensize(20)
timmy.speed("fastest")
timmy.setheading(225)
timmy.hideturtle()
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.penup()
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen.exitonclick()
