from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

score = 0
high_score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()

food = Food()

# Starting snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food.food_spawn()


play_game = True
while play_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.update()

    if snake.snake_location() == food.food_location():
        food.food_spawn()
        snake.add_segment()
        scoreboard.score += 1
        scoreboard.update()

    if snake.hit_self() or snake.hit_wall():
        snake.reset()
        scoreboard.reset()






























screen.exitonclick()
