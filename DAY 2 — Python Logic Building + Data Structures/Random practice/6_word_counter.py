'''Word Counter Pro

Take input a sentence.
Find:
total words
longest word
frequency of each word
Should be case-insensitive.
'''
from collections import Counter
sentence = input("Enter a sentence: ").lower()
s = sentence.split()
print(f"Total words in sentence is {len(s)}")
print("Longest: ", max(s, key=len))
print(Counter(s))

'''
# Another way to solve problem
# Take input sentence
sentence = input("Enter a sentence: ")

# Convert to lowercase (case-insensitive)
sentence = sentence.lower()

# Split sentence into words
words = sentence.split()

# Total number of words
total_words = len(words)

# Longest word
longest_word = max(words, key=len)

# Frequency of each word
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Output
print("Total words:", total_words)
print("Longest word:", longest_word)
print("Word frequencies:")
for word, freq in word_frequency.items():
    print(word, ":", freq)
'''