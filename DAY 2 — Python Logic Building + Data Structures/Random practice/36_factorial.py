# Factorial Calculator
# Calculate the factorial of a number (e.g., 5! = 5×4×3×2×1 = 120).

n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i

# print(factorial)

def fact(n):
    if n==0 or n==1:
        return n
    return n * fact(n-1)
print(fact(n))