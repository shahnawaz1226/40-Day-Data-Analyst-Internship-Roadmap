# Q7
# Count frequency of characters in string using dictionary.

text = "Apple"

freq_count = {}

for ch in text:
    if ch in freq_count:
        freq_count[ch]+=1
    else:
        freq_count[ch]=1

print(freq_count)