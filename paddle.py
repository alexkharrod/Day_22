from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, position):
        # draw our paddle
        self.position = position
        self.paddle = Turtle('square')
        self.paddle.speed("fastest")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.goto(position)
        self.paddle.color("white")
        self.paddle.setheading(90)




    def up(self):
        self.paddle.setheading(UP)
        self.paddle_move()


    def down(self):
        self.paddle.setheading(DOWN)
        self.paddle_move()

        # def left_up(self):
        #     self.paddle.setheading(UP)
        #     self.paddle_move()
        #
        # def left_down(self):
        #     self.paddle.setheading(DOWN)
        #     self.paddle_move()

    def paddle_move(self):
        self.paddle.forward(MOVE_DISTANCE)
