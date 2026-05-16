# Remove duplicate elements from a list (without using set)

lst = [int(x) for x in input("Enter elements seperated by spaces: ").split()]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
