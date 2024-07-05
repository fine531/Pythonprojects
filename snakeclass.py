from turtle import *
from typing import List

SNAKE_DOTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Constants declared as capitalized
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Set initial positions farther apart to avoid immediate collision
        initial_positions = [(-100, 0), (-120, 0), (-140, 0), (-160, 0), (-180, 0), (-200, 0), (-220, 0), (-240, 0), (-260, 0), (-280, 0)]
        for position in initial_positions:
            segment = Turtle(shape="square")
            segment.color("#99ffcc")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("#99ffcc")
        new_segment.penup()
        # Place the new segment at the position of the last segment
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
