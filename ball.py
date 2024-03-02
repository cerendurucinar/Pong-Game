from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.velocity = 0.1
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce(self):
        self.y *= -1

    def bounce_paddle(self):
        self.x *= -1
        self.velocity *= 0.9

    def start_over(self):
        self.home()
        self.x *= -1
        self.velocity = 0.1






