# Count frequency of each character in a string using dictionary

str = input("Enter a string: ")
dictionary = {}

for ch in str:
    if ch in dictionary:
        dictionary[ch]+=1
    else:
        dictionary[ch]=1

for keys, count in dictionary.items():
    print(keys, count)