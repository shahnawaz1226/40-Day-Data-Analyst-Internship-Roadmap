# Print sum of first n natural numbers & print factorial of a number

n = int(input("Enter a number: "))
sum = 0
factorial = 1
for i in range(1,n+1):
    sum += i
    factorial *= i
print(sum)
print(factorial)

# By using recursion
def fact(x):
    if x==0 or x==1:
        return 1
    return fact(x-1)*x

print(fact(5))