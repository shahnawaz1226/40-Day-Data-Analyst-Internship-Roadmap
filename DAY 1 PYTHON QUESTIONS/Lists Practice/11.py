# Lists Practice
# Q11
# Find maximum number in list.

nums = [32, 21, 6, 99, 45, 87, 44]

print(max(nums))

max_value = nums[0]

for i in nums:
    if i>max_value:
        max_value=i
print(f"Max value is {max_value}")