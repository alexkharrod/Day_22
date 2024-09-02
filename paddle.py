from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        # draw our paddle
        super().__init__()
        self.position = position
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")


    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)


    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)





