# import turtle
# from turtle import Turtle,Screen
#
# import prettytable
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red","green")
# turtle.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



from prettytable import PrettyTable

table = PrettyTable()
table.align="r"
table.field_names = ["Pokemon Name","Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])


print(table)