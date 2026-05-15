# Q5
# Count even and odd numbers in list.

lst = [3, 4, 1, 65, 42, 66, 73, 23, 24, 20, 2, 4, 6]

count_even = 0
count_odd = 0
for i in lst:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Evens: ", count_even)
print("Odds: ", count_odd)
