from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# STARTING_Y = randint(-250, 250) # random starting x position
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            print(new_car)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(COLORS[randint(0, 5)])
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

        # print(f" car 1: {self.all_cars[0].ycor()}")

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            print(f" car 1: {self.all_cars[0].ycor()}")
