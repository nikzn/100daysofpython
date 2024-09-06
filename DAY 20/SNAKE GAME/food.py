from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        self.score = -1
        super().__init__()
        self.create_food()



    def create_food(self):

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
