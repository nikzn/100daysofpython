from turtle import Turtle

class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.level=0
         self.update_scoreboard()

     def update_scoreboard(self):
         self.clear()
         self.penup()
         self.level+=1
         self.hideturtle()
         self.goto(-250, 250)
         self.color("black")
         self.write(f"Level :{self.level}", align="center", font=('Ariel', 18, 'bold'))


     def game_over(self):
         self.goto(0, 0)
         self.color("black")
         self.write("Game Over", align="center", font=('Ariel', 18, 'bold'))
         self.hideturtle()