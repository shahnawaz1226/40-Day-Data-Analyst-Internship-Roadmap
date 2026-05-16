# Take two sets from user and print:
# union
# intersection
# difference

set1 = {int(x) for x in input("Enter elements seperated by space: ").split()}
set2 = {int(x) for x in input("Enter elements seperated by space: ").split()}

print(f"Union: {set1 & set2}")
print(f"Union: {set1 | set2}")
print(f"Difference of Set1 - Set2: {set1 - set2}")
print(f"Difference of Set2 - Set1: {set2 - set1}")