from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.center_line()
        self.goto(-50, 100)
        self.write(self.l_score, align='center', font=('arial', 80, 'normal'))
        self.goto(50, 100)
        self.write(self.r_score, align='center', font=('arial', 80, 'normal'))

    def l_scored(self):
        self.l_score += 1

    def r_scored(self):
        self.r_score += 1

    def center_line(self):
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.color("white")
        self.setheading(270)
        for i in range(0, 30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)






