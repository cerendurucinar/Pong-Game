from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        x = self.xcor()
        if self.ycor() < 243:
            self.goto(x, y + 20)

    def move_down(self):
        y = self.ycor()
        x = self.xcor()
        if self.ycor() > -243:
            self.goto(x, y - 20)