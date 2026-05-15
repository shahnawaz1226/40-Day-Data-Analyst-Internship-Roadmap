# Q14
# Count frequency of each element.

marks = [87, 87, 97, 94, 97, 76, 56, 99, 99, 76, 56, 87]

marks_freq_count = {}

for i in marks:
    if i in marks_freq_count:
        marks_freq_count[i]+=1
    else:
        marks_freq_count[i]=1

print(marks_freq_count)