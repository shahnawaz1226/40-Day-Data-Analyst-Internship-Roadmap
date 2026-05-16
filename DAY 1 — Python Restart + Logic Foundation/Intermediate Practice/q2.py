# Match Case Statements
# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

# Write a program using match case that simulates a simple calculator:
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

day = int(input("Enter a day(1-7): "))

match day:
    case 1:
        print("It's Monday.")
    case 2:
        print("It's Tuesday.")
    case 3:
        print("It's Wednesday.")
    case 4:
        print("It's Thursday.")
    case 5:
        print("It's Friday.")
    case 6:
        print("It's Saturday.")
    case 7:
        print("It's Sunday.")

# 2----------------------------------------------------
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

operation = int(input("Choose an option to perform operation on given numbers: \nclick 1 for +\nclick 2 for -\nclick 3 for x\nclick 4 for /\nEnter option: "))

match operation:
    case 1:
        print(f"{a} + {b} = {a+b}")
    case 2:
        print(f"{a} - {b} = {a-b}")
    case 3:
        print(f"{a} x {b} = {a*b}")
    case 4:
        print(f"{a} / {b} = {a/b}")