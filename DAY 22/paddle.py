from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.shapesize(1, 5, 1)
        self.setheading(90)


    def move_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_downward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
