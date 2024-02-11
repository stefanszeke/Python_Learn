
    
from turtle import Turtle

FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self, high_score):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.color("white")
        self.update()
        
    def update(self):
        self.clear()
        self.write(f'score = {self.score}, high score = {self.high_score}', move=False, align='left', font=FONT)
        
    def increase(self):
        self.score += 1
        self.update()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER\nfinal score {self.score}', move=False, align='center', font=FONT)
    
    def reset_game(self):
        if(self.score > self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update()