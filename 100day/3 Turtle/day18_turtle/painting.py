from turtle import Turtle, Screen
import random
import colorgram


# get colors from image
colorsExtract = colorgram.extract('img2.jpeg', 12)
colorsList = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorsExtract]


# turtle setup
t = Turtle()
screen = Screen()
screen.setup(600, 600)
screen.colormode(255)

windowX = screen.window_width()
windowY = screen.window_height()

step = windowX//20

print(windowX, windowY)

t.speed(0)
t.pensize(1)



# initial position
t.penup()
t.setheading(180)
t.forward(step*10)
t.setheading(270)
t.forward(step*9)
t.setheading(0)
right = True


# main loop
for i in range(10):
    for i in range(10):
        t.color(random.choice(colorsList))
        t.forward(step)
        t.pendown()
        # t.begin_fill()
        # t.circle(15)
        # t.end_fill()
        t.dot(30)
        t.penup()
        t.forward(step)
    t.setheading(90)
    # t.forward(step*3) if right else t.forward(step)
    t.forward(step*2)
    t.setheading(180) if right else t.setheading(0)
    right = not right
        


screen.listen()
screen.exitonclick()