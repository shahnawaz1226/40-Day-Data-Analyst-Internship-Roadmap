# Count Vowels
# Ask for a word or sentence and count how many vowels (a, e, i, o, u) are in it.

word = input("Enter a word: ").lower()
vowel = "aeiou"
count = 0

for char in word:
    if char in vowel:
        count += 1
        print(char, end=" ")

print("\n",count, sep="")