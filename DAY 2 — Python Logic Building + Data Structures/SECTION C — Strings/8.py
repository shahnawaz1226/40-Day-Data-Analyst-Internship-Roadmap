# Q8
# Count vowels and consonants.

word = input("Enter a word: ").lower()
vowels = "aeiou"

vowels_count = 0
consonant_count = 0
for i in word:
    if i in vowels:
        vowels_count+=1
    else:
        consonant_count+=1

print("Vowels: ", vowels_count)
print("Consonants: ", consonant_count)
