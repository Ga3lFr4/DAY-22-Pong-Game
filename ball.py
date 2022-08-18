from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.bounces = 0
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move = - self.y_move

    def x_bounce(self):
        self.x_move = - self.x_move

    def reset_ball(self):
        self.goto(0, 0)
        self.x_bounce()

