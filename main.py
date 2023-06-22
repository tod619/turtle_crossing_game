# Turtle Crossing Game
# Game inspired by Frogger, created using the Turtle graphics library
# 22/06/2023

import time
from turtle import Screen
from player import Player
from car_manager import CareManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CareManager()
scoreboard = Scoreboard()

# Listen for player input
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect if the player makes it to the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
