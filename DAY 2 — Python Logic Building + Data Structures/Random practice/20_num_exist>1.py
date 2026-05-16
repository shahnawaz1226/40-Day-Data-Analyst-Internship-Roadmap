# Check if a number exists in a list or not
# input a list from user
# check inside if any number exist more than 1 times print error.

# lst = [float(n) for n in input("Enter elements of list seperated by commas(,): ").split(",")]
# unique = set()
# dup_lst = False
# for i in lst:
#     if i in unique:
#         print("Error! Every element should be unique in list")
#         dup_lst = True
#         break
#     unique.add(i)
# if not dup_lst:
#     print("No duplicates found. List is valid ✅")


# Take list input from user
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# seen = set()
# duplicate_found = False

# for num in numbers:
#     if num in seen:
#         print("Error: Duplicate number found ->", num)
#         duplicate_found = True
#         break
#     seen.add(num)

# if not duplicate_found:
#     print("No duplicates found. List is valid ✅")


data = list(map(float, input("Enter elements seperated by sapce: ").split()))
new_data = []
dup = 0
for num in data:
    if num not in new_data:
        new_data.append(num)

if data!=new_data:
    print("Error: Duplicate number found ->")
else:
    print("No duplicates found. List is valid ✅")