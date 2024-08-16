import random

rock = '''''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''


inputData = [rock, paper, scissor]


gameinput = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")

computterInput = random.randint(0, 1)




gameinput =int(gameinput)
computterInput=int(computterInput)

if gameinput >2:
    print("INVALID INPUT")
else:
    print(f"Your Input : {gameinput} \n {inputData[gameinput]}")

    print(f"Computer input: {computterInput} \n {inputData[computterInput]}")
    if gameinput == computterInput:
        print("DRAW")

    else:
        if gameinput == 0:
            if computterInput == 1:
                print("YOU LOSE")
            elif computterInput == 2:
                print("YOU WIN")
        elif gameinput == 1:
            if computterInput == 0:
                print("YOU WIN")
            elif computterInput == 2:
                print("YOU LOSE")
        elif gameinput == 2:
            if computterInput == 0:
                print("YOU LOSE")
            elif computterInput == 1:
                print("YOU WIN")






