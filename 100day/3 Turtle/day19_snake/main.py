from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=590, height=590)
screen.bgcolor("black")
screen.title("Sssssssssssnake")
screen.tracer(0)


high_score = 0

with open("high_score.txt", mode='r') as file:
    readScore = file.read()
    if(readScore == ''):
        high_score = 0
    else:
        high_score = int(readScore)
    
    
segments = []

snek = Snake()
fod = Food()
score = ScoreBoard(high_score)


screen.update()

screen.listen()
screen.onkey(lambda: snek.move("up"), "w")
screen.onkey(lambda: snek.move("left"), "a")
screen.onkey(lambda: snek.move("down"), "s")
screen.onkey(lambda: snek.move("right"), "d")

def write_high_score():
    with open("high_score.txt", mode='w') as file:
        file.write(str(score.high_score))

def game_loop():
    snek.snake_on()
    screen.update()
    
    if(snek.self_collision()):
        score.reset_game()
        snek.reset_snake()
        write_high_score()
    
    if(snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280):
        score.reset_game()
        snek.reset_snake()
        write_high_score()
    
    if(snek.head.distance(fod) < 25):
        fod.randomize()
        score.increase()
        snek.grow()
    
    screen.ontimer(game_loop, 100)  # Adjust the delay as needed for game speed

game_loop()  # Start the game loop












screen.exitonclick()