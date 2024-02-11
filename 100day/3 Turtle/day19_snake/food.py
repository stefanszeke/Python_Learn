from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.randomize()
    
    def randomize(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
