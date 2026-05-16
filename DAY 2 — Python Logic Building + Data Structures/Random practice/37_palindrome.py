# Palindrome Checker
# Check if a word reads the same forwards and backwards (e.g., "radar", "level").

word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"{word.capitalize()} is a palindrome.")
else:
    print(f"{word.capitalize()} is not a palindrome.")