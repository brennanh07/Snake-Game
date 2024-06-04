from turtle import Turtle
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for x in range(3):
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(STARTING_COORDINATES[x])
            self.snake_segments.append(snake_segment)

    def move(self):
        for x in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[x - 1].xcor()
            new_y = self.snake_segments[x - 1].ycor()
            self.snake_segments[x].goto(new_x, new_y)
        self.snake_segments[0].forward(20)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def snake_location(self):
        position = [round(self.head.xcor()), round(self.head.ycor())]
        return position

    def add_segment(self):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(self.snake_segments[-1].pos())
        self.snake_segments.append(snake_segment)



