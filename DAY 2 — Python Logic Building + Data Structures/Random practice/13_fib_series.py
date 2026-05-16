# Fibonacci Sequence: Find the \(n^{th}\) number in the sequence where each number is the sum of the two preceding ones. By using recursion

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a numer: "))
for i in range(n):
    print(fibonacci(i), end=" ")

# Simple method
# n = int(input("Enter a number: "))
# a,b = 0, 1
# print("Fibonacci series:", end=" ")

# for i in range(n):
#     print(a, end=" ")
#     a,b = b, a+b
