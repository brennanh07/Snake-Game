from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(0, 280)
        self.write(f"Score: {score}", align="center", font=("Arial", 12, "bold"))

    def update(self, score):
        self.write(f"Score: {score}", align="center", font=("Arial", 12, "bold"))
