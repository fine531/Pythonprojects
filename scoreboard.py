from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 320)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over ☹", align="center", font=("Arial", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
