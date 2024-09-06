import turtle
from random import random
from turtle import Turtle,Screen
from random import randint,choice

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
turtle.colormode(255)

def drawSquare():
    timmy_the_turtle.forward(90)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(90)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(90)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(90)

color =["sandy brown","blue","red","green","yellow","chartreuse"]

# drawSquare()
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

def randomColor():
    data= (randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    return data
#
#
#
# def shapes(num_size,color):
#     angle = num_size
#     for _ in range(angle):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/angle)
#
#
# for number in range(3,10):
#     color=randomColor()
#     shapes(number,color)


# direction=[0,90,120,180]
# isContinue=True
#
# while isContinue==True:
#     timmy_the_turtle.pensize(12)

#     timmy_the_turtle.color(randomColor())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(choice(direction))


for _ in range(200):
    timmy_the_turtle.color(randomColor())
    timmy_the_turtle.circle(200)
    timmy_the_turtle.left(3)
    timmy_the_turtle.speed(200)



screen=Screen()
screen.exitonclick()