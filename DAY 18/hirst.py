import turtle
import colorgram
import image
import turtle as turtle_module
import random

tim= turtle_module.Turtle()
tim.penup()
tim.hideturtle()
turtle.colormode(255)
colors = colorgram.extract('image.jpg'  , 6)


rgb_colors=[
    (123, 45, 67),
    (210, 34, 89),
    (78, 156, 233),
    (245, 189, 23),
    (34, 87, 190),
    (200, 100, 150),
    (50, 230, 90),
    (90, 40, 210),
    (120, 220, 40),
    (255, 60, 120)
]
# for colors in colors:
#     r=colors.rgb.r
#     g=colors.rgb.g
#     b=colors.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def nextLine():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(360)


for dot_count in range(1,101):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if dot_count%10==0:
        nextLine()



screen=turtle.Screen()
screen.exitonclick()