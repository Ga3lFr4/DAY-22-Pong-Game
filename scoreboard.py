from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_position, 200)
        self.score = 8
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def gain_points(self):
        self.clear()
        self.score += 1
        self.update_score_board()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} player wins. Game Over!", align=ALIGNMENT, font=FONT)
