import logo
import random

shouldPlay=input("Do you want to play a game of Blackjack? type 'y' or 'n':").lower()
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_Deck = []
user_Deck = []


def drawCard(number):
    return random.sample(card,number)

def checkScore(user_Deck,computer_Deck):
    yourScore = sum(user_Deck)
    computerScore = sum(computer_Deck)
    print(f"your final cards : {user_Deck}, final score {yourScore}")
    print(f"Computer final cards : {computer_Deck}, final score {computerScore}")
    if yourScore >= 22:
        print("YOU LOSE !!")
    elif computerScore>=22:
        print("YOU WIN !!")
    elif yourScore == computerScore:
        print("DRAW")
    elif 22 > computerScore > yourScore :
        print("YOU LOSE !!")
    elif 22>yourScore>computerScore:
        print("YOU WIN")

def computerAnotherCard(user_Deck,computer_Deck):
    computer_Deck+=drawCard(1)
    if sum(computer_Deck) < 16:
        computerAnotherCard(user_Deck, computer_Deck)
    else:
        checkScore(user_Deck,computer_Deck)

def ShouldAnotherCard(user_Deck,computer_Deck):
    shouldContinue = input("Type 'y' to get another card, Type 'n' to pass:").lower()
    if shouldContinue =='y':
        user_Deck+=drawCard(1)
        print(f"your cards : {user_Deck}, current score {sum(user_Deck)}")
        print(f"Computer's first card: {computer_Deck[0]}")

        if sum(user_Deck)<22:
            ShouldAnotherCard(user_Deck,computer_Deck)
        else:
            if 11 in user_Deck:
                    i = user_Deck.index(11)
                    user_Deck[i] = 1
                    ShouldAnotherCard(user_Deck, computer_Deck)
            else:
                checkScore(user_Deck,computer_Deck)
    elif shouldContinue == 'n':
            if sum(computer_Deck) <16:
                computerAnotherCard(user_Deck, computer_Deck)
            else:
                 checkScore(user_Deck,computer_Deck)

    else:
        print("Wrong Input!!!")

def blackJack():
    computer_Deck = drawCard(2)
    user_Deck = drawCard(2)
    totalUserDeck = sum(user_Deck)
    print(f"your cards : {user_Deck}, current score {totalUserDeck}")
    print(f"Computer's first card: {computer_Deck[0]}")
    ShouldAnotherCard(user_Deck, computer_Deck)

if shouldPlay == 'y':
    print("\n" * 100)
    print(logo.logo)
    blackJack()
else:
    print("Thanks")

