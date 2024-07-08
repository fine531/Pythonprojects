from turtle import Turtle

UPWARD = 20
DOWNWARD = 20
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.shape("square")  # Set the shape to "square"
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        new_y = self.ycor() + UPWARD
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - DOWNWARD
        self.goto(self.xcor(), new_y)
