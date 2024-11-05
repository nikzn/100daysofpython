from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_starting_line()
        self.left(90)


    def move_forward(self):
       self.forward(10)

    def go_to_starting_line(self):

        self.goto(0, -280)

    def move_backward(self):
        self.backward(10)

    def is_at_finishing_line(self):
        if self.ycor()>280:
            return True
        else:
            return False

