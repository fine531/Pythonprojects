from turtle import *
import time
from snakeclass import Snake
import random
from scoreboard import Scoreboard
from typing import List, Any

window_x = 700
window_y = 700

screen = Screen()
screen.title('Snake Game')
screen.setup(width=700, height=700)
screen.bgcolor('Black')
colormode(255)
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

game_is_on = True
screen.tracer(0)


# Fruit generator
def generate_fruit ():
    x = random.randint(-window_x // 2 + 20, window_x // 2 - 20)
    y = random.randint(-window_y // 2 + 20, window_y // 2 - 20)
    fruit = Turtle(shape='circle')
    fruit.color("red")
    fruit.penup()
    fruit.goto(x, y)
    return fruit


fruit = generate_fruit()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision code
    if snake.head.distance(fruit) < 15:
        print('Got it')
        fruit.hideturtle()
        fruit = generate_fruit()
        snake.extend()
        scoreboard.increase_score()

    # Wall hitting code
    if snake.head.xcor() > window_x // 2 or snake.head.xcor() < -window_x // 2 or \
            snake.head.ycor() > window_y // 2 or snake.head.ycor() < -window_y // 2:
        game_is_on = False
        scoreboard.game_over()

    # Collision with own body
    for segment in snake.segments[1:]:  # Start from the second segment
        if snake.head.distance(segment) < 10:
            print("Collision detected with own body!")
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
