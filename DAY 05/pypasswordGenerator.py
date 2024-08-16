import random

print("WELCOME TO PY PASSWORD GENERATOR")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '\\', '`', '~']
shufflePassword = []
password = ''
shuffledpassword = ''

nr_letter = int(input("How many letter would you like in your password? \n"))
nr_number = int(input("How many numbers would you like in your password? \n"))
nr_symbol = int(input("How many symbols do you want in your password? \n "))

nr_letters = random.sample(letters, nr_letter)
nr_numbers = random.sample(numbers, nr_number)
nr_symbols = random.sample(symbol, nr_symbol)

totalLength = (nr_letter + nr_symbol + nr_number)


for letter in nr_letters:
    shufflePassword += letter


for number in nr_numbers:
    shufflePassword.append(number)


for symbol in nr_symbols:
    shufflePassword.append(symbol)


for pwd in shufflePassword:
    password += str(pwd)

print(f"Unshuffled password: {password}")


shufflePassword = random.sample(shufflePassword, totalLength)


for pwd in shufflePassword:
    shuffledpassword += str(pwd)

print(f"Shuffled Password : {shuffledpassword}")






