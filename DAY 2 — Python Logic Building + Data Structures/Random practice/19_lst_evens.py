# Given a list:
# nums = [1, 2, 3, 4, 5, 6]
# Create a new list with only even numbers

nums = [1, 2, 3, 4, 5, 6]
even_num = []
for num in nums:
    if num%2==0:
        even_num.append(num)

print(even_num)