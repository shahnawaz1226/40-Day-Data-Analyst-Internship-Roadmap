# Sum of Numbers
# Ask the user for a number N and calculate the sum of all numbers from 1 to N.

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)