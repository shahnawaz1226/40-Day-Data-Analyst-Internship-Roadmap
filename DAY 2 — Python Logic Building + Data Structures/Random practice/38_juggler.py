# Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.

# Examples:

# Input: n = 9
# Output: 9 27 140 11 36 6 2 1
# Explaination: We start with 9 and use 
# above formula to get next terms.

def juggler(n):
    print(n, end=" ")
    
    if n==1:
        return n
    if n%2==0:
        next_n = int((n**(1/2)))
    else:
        next_n = int((n**(3/2)))
    return juggler(next_n)

n = int(input("Enter a number: "))
juggler(n)

# def juggler(n):
#     print(n, end=" ")
    
#     if n == 1:
#         return
    
#     if n % 2 == 0:
#         next_n = int(n ** 0.5)     # even → √n
#     else:
#         next_n = int(n ** 1.5)     # odd → n^(3/2)
    
#     juggler(next_n)


# # Driver code
# n = int(input("Enter n: "))
# juggler(n)
