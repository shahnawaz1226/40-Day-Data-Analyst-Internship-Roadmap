# Q4
# Find second largest element.

lst = [35, 87, 67, 56, 35, 67, 55, 45, 87]
unq_lst = list(set(lst))
lst.sort()
print("Second highest: ", unq_lst[-2])