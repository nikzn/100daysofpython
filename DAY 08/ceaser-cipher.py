
print('''

 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88


           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88                                             ''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
isRestart = True
hello =''

def ceaser(text, shiftNumber, direction):
    outputText = ''
    if direction == 'decode':
        shiftNumber *= -1
    for letter in text:
        if letter not in alphabet:
            outputText+=letter
        else:
            index = alphabet.index(letter) + shiftNumber
            index %= len(alphabet)
            outputText += alphabet[index]

    print(f"Your {direction}d word is : {outputText}")



while isRestart == True :
    direction = input("Type 'encode' to Encrypt, Type 'decode' to Decrypt \n" ).lower()
    if (direction == "encode") | (direction == "decode"):
        text = input("Enter your message \n").lower()
        shiftNumber = int(input("Type Shift number \n"))
        ceaser(text, shiftNumber, direction)
        restart = input("Type 'Yes' if you want to continue.Otherwise, type 'no' \n").lower()
        if restart == 'no':
            isRestart = False
    else:
        print("wrong Message !!")








