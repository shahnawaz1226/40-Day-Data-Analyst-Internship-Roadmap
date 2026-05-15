# Q13
# Create function that checks prime number.

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

number = 9

if is_prime(number):
    print("Prime Number")
else:
    print("Not Prime Number")