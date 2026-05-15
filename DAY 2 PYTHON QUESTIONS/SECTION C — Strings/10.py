# Q10
# Find most repeated character.

text = input("Enter a word:")

freq = {}

for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

max_char = max(freq, key=freq.get)
print("Most frequent character:", max_char, freq[max_char])