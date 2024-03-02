from turtle import Turtle


class GameOver(Turtle):
    def __init__(self, winner):
        super().__init__()
        self.winner = winner.capitalize()
        self.color("white")
        self.hideturtle()
        self.write(f"{self.winner} wins!", align="center", font=("Courier", 60, "normal"))
