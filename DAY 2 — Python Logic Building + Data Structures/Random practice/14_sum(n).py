# Sum of Natural Numbers: Calculate the sum of all integers from 1 up to 𝑛

def sum_n(n):
    if n==0:
        return n
    # return sum_n(n-1)+n
    return n + sum_n(n-1)

n = int(input("Enter a number: "))
print(sum_n(n))
# for series print
for i in range(n+1):
    print(sum_n(i), end=" ")