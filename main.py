# Turtle Crossing Game
# Game inspired by Frogger, created using the Turtle graphics library
# 22/06/2023

import time
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
