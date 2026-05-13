# Q10
# Create a function that checks palindrome.


x = input("Enter word: ").lower()
def palindrome(x):
    if x == x[::-1]:
        return "Palindrome."
    else:
        return "Not a palindrome."
    
print(palindrome(x))