# Introduction to Lists
# Create a list fruits = ["apple", "banana", "cherry"].

# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.
# Create a list of numbers from 1 to 10.

# Print the first three numbers using slicing.
# Print the last three numbers using slicing.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1]= "orange"
print(fruits)
print(len(fruits))

lst = []
for i in range(1, 11):
    lst.append(i)
    
print(lst)
print(lst[:3])
print(lst[-3:])
