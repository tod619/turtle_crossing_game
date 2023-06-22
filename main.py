# Turtle Crossing Game
# Game inspired by Frogger, created using the Turtle graphics library
# 22/06/2023

import time
from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# Listen for player input
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
