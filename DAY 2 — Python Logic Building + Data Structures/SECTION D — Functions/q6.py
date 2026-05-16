# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a,b):
    '''
    Docstring for muliply
    
    :param a: integer
    :param b: integer
    '''
    return a*b

print(multiply(3,5))
# help(multiply)

# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if b==0:
     return "Not valid"
    return a/b

print(safe_divide(6,3))
print(safe_divide(8,3))
print(safe_divide(17,4))
print(safe_divide(17,0))

import q4
print(q4.fact(8))