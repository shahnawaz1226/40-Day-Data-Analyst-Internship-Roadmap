# Q9
# Count vowels in a string.

word = input("Enter word: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count+=1
print(count)
