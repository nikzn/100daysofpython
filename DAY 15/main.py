import data
import logo
resources = data.RESOURCES
menu = data.MENU
isCoffeeStart=True

print(logo.logo)

while isCoffeeStart==True:
    def coinInput(choice,ingredient):
        total=int(input("How many quarters?:"))*0.25
        total+=int(input("How many dimes?:"))*0.10
        total+=float(input("How many nickles?:"))*0.05
        total+=float(input("How many pennies?:"))*0.01
        if total < priceList(choice):
            print("Not enough coins")
        else:
            print(f"Total:{round(total,2)}")
            change=total-priceList(choice)
            resources['amount']+=priceList(choice)
            print(f"Here is your {round(change,2)} in change")
            print(f"Here is your {choice} Enjoy !!")
            resources['water']-=ingredient['water']
            resources['coffee'] -= ingredient['coffee']
            if choice!='espresso':
                resources['milk'] -= ingredient['milk']




    def checkResource(choice,ingredient):
        global isCoffeeStart
        if ingredient["water"]>=resources["water"]:
            print("no water")
            isCoffeeStart = False
            return isCoffeeStart
        if ingredient["coffee"] >= resources["coffee"]:
            print("no coffee")
            isCoffeeStart = False
            return isCoffeeStart
        if choice !='espresso':
            if ingredient["milk"] >= resources["milk"]:
                 print("no water")
                 isCoffeeStart = False
                 return isCoffeeStart
        priceList(choice)
        coinInput(choice,ingredient)



    choice = input("What would you like? (espresso/latte/cappuccino):").lower()


    def priceList(choice):
        return menu[choice]["cost"]

    if choice =='report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Amount: {resources['amount']}")
    elif choice == 'latte':
        checkResource(choice,menu[choice]["ingredients"])
    elif choice == 'cappuccino':
        checkResource(choice, menu[choice]["ingredients"])
    elif choice == 'espresso':
        checkResource(choice, menu[choice]["ingredients"])
    else:
        print("wrong action!")
        isCoffeeStart=False

