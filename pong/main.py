from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()

ball = Ball()
scoreboard = Scoreboard()

paddle_left = Paddle(position=(-320, 0))
paddle_right = Paddle(position=(320, 0))
# Left Paddle Control
screen.onkeypress(lambda: paddle_left.start_repeat(paddle_left.up), "w")
screen.onkeyrelease(paddle_left.stop_repeat, "w")
screen.onkeypress(lambda: paddle_left.start_repeat(paddle_left.down), "s")
screen.onkeyrelease(paddle_left.stop_repeat, "s")
# Right Paddle Control
screen.onkeypress(lambda: paddle_right.start_repeat(paddle_right.up), "Up")
screen.onkeyrelease(paddle_right.stop_repeat, "Up")
screen.onkeypress(lambda: paddle_right.start_repeat(paddle_right.down), "Down")
screen.onkeyrelease(paddle_right.stop_repeat, "Down")
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 300 or    ball.distance(paddle_left) < 50 and ball.xcor() < -300:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
