from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore=0
        self.rscore=0
        self.update_scoreboard()


    def update_lpaddle(self):
        self.lscore+=1
        self.update_scoreboard()

    def update_rpaddle(self):
        self.rscore += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.color("white")
        self.write(f"{self.lscore}     {self.rscore}", align="center", font=('Ariel', 18, 'bold'))
        self.hideturtle()






    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over",align="center",font=('Ariel',18,'bold'))
        self.hideturtle()
