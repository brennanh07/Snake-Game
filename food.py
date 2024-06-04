from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def food_spawn(self):
        coordinates = []
        for x in range(-280, 300, 20):
            coordinates.append(x)
        x_spawn = random.choice(coordinates)
        y_spawn = random.choice(coordinates)
        self.teleport(x_spawn, y_spawn)

    def food_location(self):
        position = [round(self.xcor()), round(self.ycor())]
        return position


