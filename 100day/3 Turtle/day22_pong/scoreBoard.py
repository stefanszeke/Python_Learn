from turtle import Turtle

FONT = ("Consolas", 50, "normal")

class ScoreBoard:
    def __init__(self):
        self.score1 = self.create_score(-200)
        self.score2 = self.create_score(200)
        self.score1value = 0
        self.score2value = 0
        self.create_line()
        self.update()
        
    def update(self):
            self.score1.clear()
            self.score1.write(f'{self.score1value}', move=False, align='center', font=FONT)
            self.score2.clear()
            self.score2.write(f'{self.score2value}', move=False, align='center', font=FONT)
        
        
    def addScore(self, player):
        if player == 1:
            self.score1value += 1
        elif player == 2:
            self.score2value += 1
        self.update()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER\nfinal score {self.score}', move=False, align='center', font=FONT)
        
    
    def create_score(self,x):
        score = Turtle()
        score.hideturtle()
        score.penup()
        score.goto(x, 210)
        score.color("white")
        return score
    
    def create_line(self):
        line = Turtle()
        line.penup()
        line.shape("square")
        line.pensize(5)
        line.color("white")
        line.goto(0, 300)
        line.setheading(270)
        for _ in range(16):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)
    