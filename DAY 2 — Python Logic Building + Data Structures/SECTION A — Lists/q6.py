# Write a program that takes a list of numbers and removes all duplicates using a set.


lst = []
x = int(input("Enter how many elements you want in set: "))
for i in range(x):
    a = int(input(f"Enter {i+1} element: "))
    lst.append(a)

print(set(lst))