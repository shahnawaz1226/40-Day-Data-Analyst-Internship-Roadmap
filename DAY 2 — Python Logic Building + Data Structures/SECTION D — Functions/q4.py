# Recursion in Python
# Write a recursive function factorial(n) that returns the factorial of a number.
# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def fact(n):
    if n==1 or n== 0:
        return 1
    return fact(n-1)*n

print(fact(5))

# Sum of first n natural number
def sum_of_digits(n):
    if n == 0:
        return n
    return sum_of_digits(n-1)+n

print(sum_of_digits(100))

# Sum of everyDigit in a number
def digitSum(a):
    if a==0:
        return 0
    return digitSum(a//10) + a%10

print(digitSum(8787))

# Fibonacci Series
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 0 1 1 2 3 5 8
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

a = int(input("Enter number till you want fibonacci series: "))
for i in range(a+1):
    print(fibonacci(i), end=" ")