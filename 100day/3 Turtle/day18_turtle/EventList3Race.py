from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=700, height=400)




finishLine = Turtle()
finishLine.speed(0)
finishLine.penup()
finishLine.setpos(300, 150)
finishLine.setheading(270)
finishLine.pendown()
finishLine.forward(300)

turtles = []

colors = ['blue', 'red', 'green']
yPos = [100, 0, -100]
for i in range(1, 4):
    t = Turtle()
    t.penup()
    t.shape('turtle')
    t.color(colors[i-1])
    t.setpos(-300, yPos[i-1])
    turtles.append(t)
    


input = screen.textinput("make a bet", "Who will win? (b)lue, (r)ed, (g)reen)  x to exit")
while input not in ['blue', 'red', 'green', 'b', 'r', 'g', 'x']:
    input = screen.textinput("make a bet", "Who will win? (b)lue, (r)ed, (g)reen)  x to exit")
    
if input == 'x':
    screen.bye()
    
def endRace():
    end = False
    for t in turtles:
        if t.pos()[0] >= 300:
            end = True
            break
    return end

def winner():
    for t in turtles:
        if t.pos()[0] >= 300:
            return t.color()[0]

def move():
    t = random.choice(turtles)
    t.forward(random.randint(1, 20))
    
while not endRace():
    move()



if(winner()[0] == input[0]):
    screen.textinput("You win!", "nice")
else:
    screen.textinput("You lose!", "lol")
screen.bye()



screen.exitonclick()