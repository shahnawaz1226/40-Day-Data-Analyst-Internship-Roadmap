# Q3
# Remove duplicates from list WITHOUT using set.

lst = [35, 87, 67, 56, 55, 45, 87]
unique_lst = []

for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)

print(unique_lst)