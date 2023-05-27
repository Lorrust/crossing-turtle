import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Turtle")

player = Player()
scoreboard = Scoreboard()
level = 0

car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "space")

game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    player.is_at_finish_line()
    
    #Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    #Detect successful crossing    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()