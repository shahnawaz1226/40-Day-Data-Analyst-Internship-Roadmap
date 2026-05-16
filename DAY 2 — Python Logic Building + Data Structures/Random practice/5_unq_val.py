'''Unique Values Finder

Take multiple inputs from user.
Output:
unique numbers only
duplicates count
Hint: sets + loops
'''
n= list(map(int, input("Enter numbers seperated by comma: ").split(",")))
# n = [int(x) for x in input("Enter numbers seperated by comma: ").split(",")]
print(f"Set of unique numbers: {set(n)}")
print(f"Total Duplicates: {len(n)-len(set(n))}")