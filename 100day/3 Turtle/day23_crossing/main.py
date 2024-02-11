import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
cars.create_cars(20)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    
    cars.move_cars()
    
    
    for car in cars.car_list:
        if(car.distance(player) < 20):
            player.hit_car()
    
    if(player.ycor() > 280):
        if(player.hit_finish()):
            cars.increase_speed()
    
    time.sleep(0.1)
    screen.update()

screen.exitonclick()