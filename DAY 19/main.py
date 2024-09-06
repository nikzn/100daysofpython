from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500,height=500)
import random
is_race_on=False
color=["red","orange","green","yellow","blue","purple"]
y_position=[-150,-100,-50,0,50,100]
  # a.forward(random.choice(forward))
choice = screen.textinput(title="Make your bet",prompt="Which tutle will win the race? Enter the color")
turtleList=[]

for turtle_index in range(0,6):
    a = Turtle(shape="turtle")
    a.penup()
    a.color(color[turtle_index])
    a.goto(x=-230, y=y_position[turtle_index])
    turtleList.append(a)

if choice:
    is_race_on=True


while is_race_on:
    for turtle in turtleList:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==choice:
                print(f"You've won! the {winning_color} turtle is the winner")

            else:
                print(f"You've Lost! the {winning_color} turtle is the winner")
        distance= random.randint(0,10)
        turtle.forward(distance)










screen.exitonclick()