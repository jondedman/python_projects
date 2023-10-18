from turtle import Turtle, Screen
from time import sleep

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.speed("fastest")
        self.repeat = False
        self.repeat_rate = 10


    def start_repeat(self, func):
        """
        Turns Key Repeat ON.
        Calls the function passed to it -  move_up() or move_down().

        :param func: The lambda function is passed from onkeypress()
        """
        if not self.repeat:
            self.repeat = True
            func()

    def stop_repeat(self):
        """
        Turn Key Repeat OFF
        """
        self.repeat = False

    def up(self):
        if self.ycor() < 250:
            self.forward(10)
            if self.repeat:
                Screen().ontimer(self.up, self.repeat_rate)

    def down(self):
        if self.ycor() > -250:
            self.backward(10)
            if self.repeat:
                Screen().ontimer(self.down, self.repeat_rate)
