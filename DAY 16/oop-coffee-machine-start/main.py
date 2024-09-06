from getopt import getopt
from optparse import make_option

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
# menuItem = MenuItem()

is_on=True
while is_on:
    options=menu.get_items()
    choice =input(f"what would you like ({options}): ")
    if choice =="off":
        is_on=False
    elif choice =='report':
        print(coffeeMaker.report())
        print(moneyMachine.report())
    else:
        drink=menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
           coffeeMaker.make_coffee(drink)
