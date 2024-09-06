import data
import random
import logo

DATA = data.instagramFollowers

print(logo.logo)
print(logo.VS)
score = 0
def mostFollowers(aValue,bvalue):
    aFollowers=aValue['followers']
    bFollowers=bvalue['followers']
    if aFollowers > bFollowers:
        return 'a'
    elif aFollowers < bFollowers:
        return 'b'


def isTrue(aValue,bValue,choose):
    global score
    if choose == mostFollowers(aValue,bValue):
       DATA.remove(aValue)
       aValue = bValue
       score+=1
       print(f"Points:{score}")
       bValue = random.choice(DATA)
       higherorLower(aValue,bValue)
    else:
      print(f"you lose!! Final Score : {score} ")


def higherorLower(aValue,bValue):




    choose = input(f"{aValue['name']} from {aValue['country']}  have 'Higher' or 'lower' followers than \n{bValue['name']} from {bValue['country']} ?\n TYPE 'A' for higher or 'B' for lower :").lower()
    isTrue(aValue,bValue,choose)


def randoms():
    aValue = random.choice(DATA)
    bValue = random.choice(DATA)
    if aValue == bValue:
        bValue=random.choice(DATA)
    higherorLower(aValue,bValue)



randoms()




