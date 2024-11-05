from importlib.resources import contents
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=self.read_text()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score:{self.score}   High Score:{self.high_score} "   , align="center", font=('Ariel', 13, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.write_high_score()
        self.update_scoreboard()

    def read_text(self):
        with open("high_score.txt") as file:
            content=int(file.read())
            return content

    def write_high_score(self):
        with open("high_score.txt",mode='w') as file:
            file.write(f"{self.high_score}")



    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over !!", align="center", font=('Courier', 15, 'bold'))

    def increase_score(self):
        self.score+=1

        self.update_scoreboard()