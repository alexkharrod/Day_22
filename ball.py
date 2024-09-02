from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1




    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def y_bounce(self):
        self.y_move *= -1
        if self.sleep_time >= .01:
            self.sleep_time -= .01


    def x_bounce(self):
       self.x_move *= -1

    def out_of_bounds(self):
        self.goto(0,0)
        self.x_bounce()
        self.sleep_time = 0.1


