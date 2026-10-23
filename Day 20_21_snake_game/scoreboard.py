from turtle import Turtle
alignment = "center"
font = ("courier", 24, "normal") # font for the scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()

        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard() # update the scoreboard after incrementing the score

    def game_over(self): 
        self.goto(0,0)
        self.write(
            "Game Over", 
            align="center", 
            font=("Arial", 30, "normal")
            )

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}", 
            align="center",
            font=("Arial", 24, "normal")
        )