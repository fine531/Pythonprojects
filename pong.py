from turtle import Screen
from pongpeddle import Paddle
from pongball import Ball
from pong_scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# Create paddles
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreB = Scoreboard()

# Keybindings
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
is_game_on = True
while is_game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Detect the collision of ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect the contact with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect R_side ball miss with paddle situation
    if ball.xcor() > 380:
        ball.reset_position()
        scoreB.l_point()

    #Detect l_side ball miss with paddle situation
    if ball.xcor() < -380:
        ball.reset_position()
        scoreB.r_point()
screen.exitonclick()
