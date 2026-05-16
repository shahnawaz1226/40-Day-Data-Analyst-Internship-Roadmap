'''Basics & Data Types

Take two numbers from user and print:
sum
difference
product
division (2 decimal places)'''

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
# For 2 decimal places
result = round(num1/num2, 2)
print(f"{num1} / {num2} = {result}")