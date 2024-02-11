from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
t.pensize(10) 
screen = Screen()
screen.listen()
t.color('red')
        
t.penup()

def togglePen():
    if t.isdown():
        t.penup()
        t.color('red')
    else:
        t.pendown()
        t.color('blue')


def moveForward():
    t.forward(10)

def rotateLeft():
    t.left(10)
    
def rotateRight():
    t.right(10)
    
def reset():
    t.reset()
    t.penup()
    t.home()
    t.speed(0)
    t.pensize(10) 
    t.color('red')



screen.onkey(moveForward, 'w')
screen.onkey(rotateLeft, 'a')
screen.onkey(rotateRight, 'd')
screen.onkey(togglePen, 'space')
screen.onkey(reset, 'r') 

t2 = Turtle()
t2.speed(1)
t2.pensize(10)
t2.color('green')
t2.setheading(90)
t2.forward(300)




screen.exitonclick()