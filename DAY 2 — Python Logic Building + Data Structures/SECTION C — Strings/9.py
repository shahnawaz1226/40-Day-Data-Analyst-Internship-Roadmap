# Q9
# Check palindrome.

text = input("Enter a word:").lower()

rev_text = ""

for i in text:
    rev_text = i + rev_text
if text == rev_text:
    print("Palindrome")
else:
    print("Not a palindrome")