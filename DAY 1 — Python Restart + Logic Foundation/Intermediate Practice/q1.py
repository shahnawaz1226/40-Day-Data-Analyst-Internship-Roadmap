# 1. If-Else Conditional Statements
# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
# Create a program that checks if a person is eligible to vote (age >= 18).
# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

number = int(input("Enter a number: "))
# 1
if number==0:
    print("It's Zero.")
elif number>0:
    print("It's a positive number.")
else:
    print("It's a negative number.")

# 3
if number%2==0:
    print("It is an even number.")
else:
    print("It is an odd number.")


# 2
num = int(input("Enter your age: "))
if num>=18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")
