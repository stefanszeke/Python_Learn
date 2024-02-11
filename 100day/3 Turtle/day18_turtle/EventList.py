from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
t.pensize(10) 
screen = Screen()
screen.listen()

t.penup()

def togglePen():
    if t.isdown():
        t.penup()
        t.color('red')
    else:
        t.pendown()
        t.color('blue')


def moveUp():
    t.setheading(90)
    t.forward(10)

def moveDown():
    t.setheading(270)
    t.forward(10)
    
def moveLeft():
    t.setheading(180)
    t.forward(10)

def moveRight():
    t.setheading(0)
    t.forward(10)

screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(togglePen, 'space')



screen.exitonclick()