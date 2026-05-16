# Take 5 numbers from user and store in a list:
# print max & min
# print sum & average

nums = [float(x) for x in input("Enter nums seperated by space: ").split()]

# print(nums)x
print("Minimum: ", min(nums))
print("Maximum: ", max(nums))
print("Sum: ", sum(nums))
print("Average: ", sum(nums)/len(nums))

# Without using in-buit function like sum(), min(), max()
minimum = nums[0]
maximum = nums[0]
sum = 0
count = 0
for i in nums:
    if i<minimum:
        minimum = i
    if i>maximum:
        minimum = i
    sum+=i
    count+=1

print("Minimum: ", minimum)
print("Maximum: ", maximum)
print("Sum: ", sum)
print("Average: ", sum/count)