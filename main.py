from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.title("Snake Game")
screen.bgcolor("khaki")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True

while is_game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake collision with the food.
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect snake collision with the wall.
    if snake.snake_head.xcor() > 330 or snake.snake_head.xcor() < -330 or snake.snake_head.ycor() > 310 or snake.snake_head.ycor() < -330:
        score.reset()
        snake.reset()

    # Detect snake collision with the tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 15:
            score.reset()
            snake.reset()

screen.exitonclick()
