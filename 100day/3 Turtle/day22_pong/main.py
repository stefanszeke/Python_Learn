from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()


paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball()
scoreBoard = ScoreBoard()


screen.update()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

screen.onkey(screen.bye, "Escape")


def game_loop():
    
    if(ball.distance(paddle2) < 40):
        ball.bounce()
    elif(ball.distance(paddle1) < 40):
        ball.bounce()
        
    if(ball.xcor() > 395):
        ball.reset_position(False)
        scoreBoard.addScore(1)
    elif(ball.xcor() < -395):
        ball.reset_position(True)
        scoreBoard.addScore(2)
        
    ball.move()
    screen.update()

    
    screen.ontimer(game_loop, ball.gameSpeed)  # Adjust the delay as needed for game speed
game_loop()  # Start the game loop

screen.mainloop()