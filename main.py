from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake_segments = []

# Starting snake
starting_xcoordinates = [0, -20, -40]
for x in range(3):
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.setx(starting_xcoordinates[x])
    snake_segments.append(snake_segment)

screen.update()


def change_direction():
    for segment in snake_segments:
        segment.setheading(90)


while True:
    screen.update()
    time.sleep(0.1)
    for x in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[x - 1].xcor()
        new_y = snake_segments[x - 1].ycor()
        snake_segments[x].goto(new_x, new_y)
    snake_segments[0].forward(20)


















screen.exitonclick()
