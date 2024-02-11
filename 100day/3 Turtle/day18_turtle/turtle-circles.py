from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

t.speed(0)
t.pensize(1)

def randomColorTuple():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    
def drawCircles(step):
    for i in range(360//step):
        t.pencolor(randomColorTuple())
        t.circle(100)
        t.left(step)
        

def drawCircles2(step):
    startSize = 100
    for i in range(360//step):
        t.pencolor(randomColorTuple())
        t.circle(startSize)
        t.left(step)
        startSize -= (100/(360//step))

def drawCircles3(step):
    startSize = 1
    for i in range(360//step):
        t.pencolor(randomColorTuple())
        t.circle(startSize)
        t.left(step)
        startSize += (100/(360//step))
        
drawCircles(5)
# drawCircles2(5)
# drawCircles3(5)














screen.listen()
screen.exitonclick()