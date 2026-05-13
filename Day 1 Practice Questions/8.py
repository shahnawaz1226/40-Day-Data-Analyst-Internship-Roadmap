# Q8
# Reverse a string without using slicing.

string = input("Enter a word: ")

# print(string[::-1])
reversed_str = ""
for char in string:
    reversed_str = char + reversed_str
print(reversed_str)
