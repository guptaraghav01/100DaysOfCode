from turtle import Turtle
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("E:\\Extra\\Python\\100DaysOfCode\\day_24\\snake_game_with_highscore\\data.txt") as file:
    score = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.goto(x=0, y=265)
        self.score = 0
        with open("E:\\Extra\\Python\\100DaysOfCode\\day_24\\snake_game_with_highscore\\data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E:\\Extra\\Python\\100DaysOfCode\\day_24\\snake_game_with_highscore\\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
