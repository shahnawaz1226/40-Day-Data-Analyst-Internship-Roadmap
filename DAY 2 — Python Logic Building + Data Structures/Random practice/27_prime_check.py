# Write a function to check prime number

def is_prime(n):
    for i in range(2, n+1):
        if n==2:
            return f"{n} is a prime number."
        elif n%i == 0:
            return f"{n} is not a prime number."
        else:
            return f"{n} is a prime number."

        
n = int(input("Enter a number: "))
print(is_prime(n))

# Another method
# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True
