from turtle import Turtle
ALIGNMENT = "center"
FONT_DESIGN = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Score_data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.color("medium purple")
        self.penup()
        self.goto(x=0, y=320)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score={self.high_score}", align=ALIGNMENT,
                   font=FONT_DESIGN)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Score_data.txt", "w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()
