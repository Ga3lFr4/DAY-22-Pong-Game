from turtle import Turtle

UP_LIMIT = 250
DOWN_LIMIT = - 250

class Paddle(Turtle):

    def __init__(self, start_coor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(start_coor)

    def up(self):
        if self.ycor() < UP_LIMIT:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > DOWN_LIMIT:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
