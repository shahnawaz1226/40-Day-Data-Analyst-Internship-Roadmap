# Q12
# Remove duplicates from list.

marks = [87, 97, 94, 76, 56, 76, 56, 87]

# print(set(marks))

unique_marks_list = []
for i in marks:
    if i not in unique_marks_list:
        unique_marks_list.append(i)

print(unique_marks_list)