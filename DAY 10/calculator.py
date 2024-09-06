import logo
print(logo.logo)
print(logo.logoCalulator)
result = 0

def calculate(first_number,second_number,operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation =='/':
        return first_number / second_number
    else:
        print("Invalid Operation")

def calcultor():
    isContinue = True
    first_number = float(input("Input First Number:"))
    while isContinue == True:
        print("Pick an operation \n")
        print("+\n-\n*\n/")
        operation = input()
        second_number = float(input("Enter the second number"))
        result = calculate(first_number,second_number,operation)
        print(f"{first_number} {operation} {second_number} = {result}")
        shouldContinue = input(f"Type 'y' to continue with {result}. Type 'n' to start new calculation ").lower()
        if shouldContinue =='y':
            first_number = result
        else:
            result = 0
            calcultor()

calcultor()