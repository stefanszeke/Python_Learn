from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.createBall()
        self.movingUp = True
        self.movingRight = True
        self.ballSpeed = 10
        self.y_move = 10
        self.x_move = 10
        self.gameSpeed = 100
        
    def createBall(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)
        
    def move(self):
        if(self.ycor() > 280 or self.ycor() < -280):
            self.y_move *= -1
        
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.x_move *= -1
        self.gameSpeed = int(self.gameSpeed * 0.9)

        
    def reset_position(self, right):
        self.setpos(0, 0)
        self.movingRight = right
        self.movingUp = True
        self.gameSpeed = 100
        