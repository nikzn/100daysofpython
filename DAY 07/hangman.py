import random
import hangmanStages
import hangmanWords

placeholder =''
lives = -1
totalLives =7
gameOver = False
correct_letters = []
randomWord = random.choice(hangmanWords.word_Set)
for let in randomWord:
    placeholder += '_'

print(hangmanStages.hangManArt)

print(placeholder)


while not gameOver:
    user_Letter = input("Guess a letter: \n").lower()
    word = ''
    if user_Letter in correct_letters:
        print("You Already Guessed this letter")

    if not user_Letter in randomWord:
        print("########################################### WRONG LETTER ###########################################")
        print(f"You Guessed {user_Letter}. Not in the Word.You lose a LIFE")
        lives+=1
        totalLives-=1
        print(f"You Have {totalLives} lives Left !!")
        if lives ==6:
            gameOver = True
            print("########################################### YOU LOSE ###########################################")

    else:
        for letter in randomWord:
            if letter == user_Letter:
                word += letter
                correct_letters.append(letter);
            elif letter in correct_letters:
                word +=letter
            else:
                word += '_'
        print(word)

        if "_" not in word:
            gameOver = True
            print("########################################### YOU WIN !! ###########################################")

    print(hangmanStages.HANGMANPICS[lives])