# String Formatting and f-Strings
# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

# Do the same using f-strings.

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")
sentence = "My name is {} and I am {} years old."

print(sentence.format(name, age))