
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.create_paddle(x)

    def create_paddle(self, x):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x, 0)
    
    def move_up(self):
        if(self.ycor() < 250):
            self.sety(self.ycor() + 20)

    def move_down(self):
        if(self.ycor() > -250):
            self.sety(self.ycor() - 20)
        