from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(0, 280)
        self.write("Score: 0", align="center", font=("Arial", 12, "bold"))

    def update(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial", 12, "bold"))
