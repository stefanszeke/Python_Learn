from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

t.speed(0)
t.pensize(25)

def randomColorTuple():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for i in range(100):
    t.pencolor(randomColorTuple())
    t.left(random.randint(0, 3)*90)
    t.forward(50)


















screen.listen()
screen.exitonclick()