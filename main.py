from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import ScoreBoard
from gameover import GameOver

screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        scoreboard.l_score += 1
        scoreboard.update_score()
        ball.start_over()

    if ball.xcor() < -380:
        scoreboard.r_score += 1
        scoreboard.update_score()
        ball.start_over()

    if scoreboard.r_score == 5:
        game_on = False
        winner = "right"

    if scoreboard.l_score == 5:
        game_on = False
        winner = "left"


if winner == "right":
    ball.hideturtle()
    game_over = GameOver("right")

elif winner == "left":
    ball.hideturtle()
    game_over = GameOver("left")






screen.exitonclick()
