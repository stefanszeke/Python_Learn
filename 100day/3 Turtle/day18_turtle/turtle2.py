from turtle import Turtle, Screen
import random


t = Turtle()



for _ in range(100):

    t.left(random.randint(0, 360))
    t.forward(random.randint(0, 100))
