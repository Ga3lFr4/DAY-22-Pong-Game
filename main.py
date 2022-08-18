import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard(100)
l_scoreboard = Scoreboard(-100)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "z")
screen.onkey(l_paddle.down, "s")

game_is_on = True
game_speed = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.move_speed *= 0.9

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        ball.move_speed = 0.1
        time.sleep(1)
        l_scoreboard.gain_points()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.move_speed = 0.1
        ball.reset_ball()
        time.sleep(1)
        r_scoreboard.gain_points()

    if r_scoreboard.score == 10:
        l_scoreboard.clear()
        r_scoreboard.game_over("Right")
        game_is_on = False
    if l_scoreboard.score == 10:
        r_scoreboard.clear()
        l_scoreboard.game_over("Left")



screen.exitonclick()