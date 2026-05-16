"""
Mini Calculator (No Drama)
User se 2 numbers + operator (+ - * /) le.
Invalid operator ho toh proper message.
"""

# 1. Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Ask the user to choose an operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# 3. Perform the operation and display the result
if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please choose a valid operation.")


    