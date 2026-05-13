# Q13
# Find second largest element.

marks = [87, 87, 97, 94, 97, 76, 56, 99, 99, 76, 56, 87]
unique_lst = list(set(marks))
unique_lst.sort()
print(unique_lst[-2])