# Pong Game
import time

from turtle import Turtle, Screen

from paddle import Paddle

from ball import Ball

from scoreboard import Scoreboard


STARTING_POSITIONS = [(350,0),  (-350, 0)]

screen =  Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)


r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()
sleep_time = 0.1

game_is_on = True
while game_is_on:
    # get paddles to move up and down

    time.sleep(ball.sleep_time)
    screen.listen()
    screen.onkey(r_paddle.up,"Up")
    screen.onkey(r_paddle.down,"Down")
    screen.onkey(l_paddle.up,"w")
    screen.onkey(l_paddle.down,"s")
    ball.move()

    if ball.ycor()  > 280 or ball.ycor() < -280:
        ball.y_bounce()

    elif ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.x_bounce()
        sleep_time -= .01

    if ball.xcor() > 380:
        scoreboard.l_scored()
        scoreboard.print_score()
        ball.out_of_bounds()

    if ball.xcor() < -380:
        scoreboard.r_scored()
        scoreboard.print_score()
        ball.out_of_bounds()

    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        game_is_on = False

    screen.update()







# Draw line in middle of screen

# Create Score on left and SCore on Right

# Draw ball and make it bounce of edge of  Lower screen

# make ball bounce off of paddles

# if  ball  goes off-screen opposite player score increases

screen.exitonclick()