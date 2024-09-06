from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:



    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in self.starting_position:
           self.add_segments(position)

    def add_segments(self,position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)



    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)



