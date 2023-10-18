from turtle import Screen

from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

padl = Paddle((-350, 0))
padr = Paddle((350, 0))





screen.listen()
screen.onkey(padl.up, "w")
screen.onkey(padl.down, "s")

screen.onkey(padr.up, "Up")
screen.onkey(padr.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # ball.move()




screen.exitonclick()
