import random
print('''      

 .d8888b.  888     888 8888888888 .d8888b.   .d8888b.       88888888888 888    888 8888888888      888b    888 888     888 888b     d888 888888b.   8888888888 8888888b.  
d88P  Y88b 888     888 888       d88P  Y88b d88P  Y88b          888     888    888 888             8888b   888 888     888 8888b   d8888 888  "88b  888        888   Y88b 
888    888 888     888 888       Y88b.      Y88b.               888     888    888 888             88888b  888 888     888 88888b.d88888 888  .88P  888        888    888 
888        888     888 8888888    "Y888b.    "Y888b.            888     8888888888 8888888         888Y88b 888 888     888 888Y88888P888 8888888K.  8888888    888   d88P 
888  88888 888     888 888           "Y88b.     "Y88b.          888     888    888 888             888 Y88b888 888     888 888 Y888P 888 888  "Y88b 888        8888888P"  
888    888 888     888 888             "888       "888          888     888    888 888             888  Y88888 888     888 888  Y8P  888 888    888 888        888 T88b   
Y88b  d88P Y88b. .d88P 888       Y88b  d88P Y88b  d88P          888     888    888 888             888   Y8888 Y88b. .d88P 888   "   888 888   d88P 888        888  T88b  
 "Y8888P88  "Y88888P"  8888888888 "Y8888P"   "Y8888P"           888     888    888 8888888888      888    Y888  "Y88888P"  888       888 8888888P"  8888888888 888   T88b 
 
 
   
                                                                                                    ________
                                                                                                _jgN########Ngg_
                                                                                              _N##N@@""  ""9NN##Np_
                                                                                             d###P            N####p
                                                                                             "^^"              T####
                                                                                                               d###P
                                                                                                            _g###@F
                                                                                                         _gN##@P
                                                                                                       gN###F"
                                                                                                      d###F
                                                                                                     0###F
                                                                                                     0###F
                                                                                                     0###F
                                                                                                     "NN@'
                                                                                        
                                                                                                      ___
                                                                                                     q###r
                                                                                                      ""
              
              ''')
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
attempts =0
number=random.randrange(1, 100)
guess=0


def guessNumber(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a Guess : "))
        print(guess)
        if guess == number:
           return print("you guessed right . you win!!")
        elif guess > number:
            print("Too High")
            attempts -= 1
        elif guess < number:
            attempts -= 1
            print("Too Low")
    if attempts == 0:
        print("Attempts Over!! You Lose ")

def difficultyMode(difficulty):
    print(number)
    if difficulty == 'easy':
        attempts = 10
        guessNumber(attempts)
    elif difficulty == 'hard':
        attempts = 5
        guessNumber(attempts)
    else:
        return print("Invalid Action !!")








difficultyMode(difficulty)