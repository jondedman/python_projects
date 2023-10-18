from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.setheading(45)
        self.speed("fastest")
        self.move_speed = 0.1

    def move(self):
        self.forward(10)
        # self.bounce()

    def bounce_y(self):
        self.setheading(self.heading() * -1)

    def bounce_x(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
