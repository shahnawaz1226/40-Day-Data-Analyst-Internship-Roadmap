# DAY 2 BONUS CHALLENGE (IMPORTANT)
# Anagram Checker
# Check whether two strings are anagrams.
# Example:
# listen
# silent


text = input("Enter a word: ").lower()
text2 = input("Enter a word: ").lower()

if sorted(text)==sorted(text2):
    print("Anagram.")
else:
    print("Not anagram.")


# TODAY’S INTERVIEW FOCUS

# Companies may ask:

# Difference between list and tuple?
# Why use dictionary?
# Difference between list and set?
# Why functions important?

# Prepare short practical answers.


# 1. Difference between List and Tuple?
# List is mutable → data change kar sakte ho.
# Tuple is immutable → once created, change nahi hota.
# Practical Example:
# my_list = [1, 2, 3]
# my_list.append(4)   # possible

# my_tuple = (1, 2, 3)
# # my_tuple.append(4) ❌ error
# Interview Line:

# “List use karta hu jab data frequently change hona ho. Tuple use karta hu jab fixed data securely store karna ho.”

# 2. Why use Dictionary?

# Dictionary key-value pair me data store karta hai, aur fast searching ke liye useful hota hai.

# Practical Example:
# student = {
#     "name": "Shahnawaz",
#     "age": 20
# }

# print(student["name"])
# Interview Line:

# “Dictionary tab use karta hu jab kisi value ko unique key ke through quickly access karna ho.”

# 3. Difference between List and Set?
# List ordered hoti hai aur duplicate values allow karti hai.
# Set unordered hota hai aur duplicates remove karta hai.
# Practical Example:
# my_list = [1, 1, 2, 3]

# my_set = {1, 1, 2, 3}

# print(my_list)  # [1, 1, 2, 3]
# print(my_set)   # {1, 2, 3}
# Interview Line:

# “Set mainly duplicate values remove karne aur unique data maintain karne ke liye use karta hu.”

# 4. Why are Functions Important?

# Functions code ko reusable, clean, aur manageable banate hain.

# Practical Example:
# def greet(name):
#     return f"Hello {name}"

# print(greet("Shahnawaz"))
# Interview Line:

# “Functions repetitive code ko avoid karte hain aur large projects ko modular aur easy-to-maintain banate hain.”