from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(0)
screen = Screen()
screen.colormode(255)

def drawDashes(n):
    for _ in range(n):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        


def drawShape(sides):
    for _ in range(sides):
        drawDashes(5)
        t.left(360/sides)
        




for i in range(10, 2, -1):

    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    colors1 = (color1, color2, color3)
    t.pencolor(colors1)
    
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    t.fillcolor(color1, color2, color3)
    
    t.begin_fill()
    drawShape(i)
    t.end_fill()











screen.listen()
screen.exitonclick()