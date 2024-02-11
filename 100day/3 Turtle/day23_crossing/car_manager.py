from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list:Turtle = []
        
    def create_cars(self, n:int):
        for _ in range(n):
            self.create_car()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(COLORS[random.randint(0, 5)])
        car.setheading(180)
        car.setx(random.randint(300, 1200))
        car.sety(random.randint(-250, 250))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        self.car_list.append(car)

    def reset_car(self, car):
        car.setx(random.randint(300, 1200))
        car.sety(random.randint(-250, 250))
        car.color(COLORS[random.randint(0, 5)])
        
    def move_cars(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)
            if(car.xcor() < -300):
                self.reset_car(car)
                
    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)
