from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"score:{self.score}", align="center", font=('Ariel', 13, 'bold'))

    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over !!", align="center", font=('Courier', 15, 'bold'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()