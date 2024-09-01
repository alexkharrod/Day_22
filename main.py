# Pong Game

from turtle import Turtle, Screen

from paddle import Paddle

import time

from random import randint

STARTING_POSITIONS = [(350,0),  (-350, 0)]



screen =  Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
# screen.tracer(0)


r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])

game_is_on = True
# while game_is_on:
    # get paddles to move up and down
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

screen.update()







# Draw line in middle of screen

# Create Score on left and SCore on Right

# Draw ball and make it bounce of edge of  Lower screen

# make ball bounce off of paddles

# if  ball  goes off-screen opposite player score increases

screen.exitonclick()