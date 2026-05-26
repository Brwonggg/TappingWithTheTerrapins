from turtle import Turtle
import random
from scoreboard import Scoreboard

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        spawn_rate = random.randint(1,4)
        if spawn_rate == 1:
            new_car = Turtle("square")
            new_car.showturtle()
            new_car.color(random.choice(COLORS))
            car_len = random.randint(2,4)
            new_car.shapesize(stretch_len=car_len)
            new_car.penup()
            new_car.setheading(180)
            random_ycor = random.randint(-300,300)
            new_car.goto(350,random_ycor)
            random_speed = random.randint(2,5)
            new_car.speed(random_speed)
            self.all_cars.append(new_car)

    def move_all(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)



