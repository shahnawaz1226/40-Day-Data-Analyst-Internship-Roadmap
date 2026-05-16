# Write a program that counts how many vowels are in a given string.
# Take a user input string and check if it is a palindrome (same forwards and backwards).

str = input("Enter String: ")

if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count Vowels
vowel = ["a", "e", "i", "o", "u"]

sum = 0 
for i in str.lower():
    if i in vowel:
        sum+=1

print(sum)