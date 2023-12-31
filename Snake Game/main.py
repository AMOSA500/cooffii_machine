from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title(titlestring='My Snake Game')
screen.bgcolor('black')
screen.setup(width=500, height=500)
screen.tracer(False)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    distance_cor_snake = snake.segments[0].distance(food)
    if distance_cor_snake < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_point()

    # Detect collision with wall
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        scoreboard.game_over()
        is_game_on = False

    # Detection collision with body
    for body in snake.segments[1:]:
        if snake.head.distance(body) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
