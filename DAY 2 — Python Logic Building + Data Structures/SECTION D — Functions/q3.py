# Lambda Functions
# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

add = lambda x,y : x+y
print(add(2,3))

square = lambda x: x**2
lst = [1, 2, 3, 4, 5]

print(list(map(square, lst)))