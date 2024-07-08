from turtle import Turtle

#Ball class : creation of ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.penup()
        self.goto(0, 0)
        self.x_pos = 15
        self.y_pos = 15
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

     #Bounce when hit the wall
    def bounce_y(self):
        self.y_pos *= -1

    #Bounce when paddle hit
    def bounce_x(self):
        self.x_pos *= -1
        self.speed *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.speed = 0.1
        self.bounce_x()