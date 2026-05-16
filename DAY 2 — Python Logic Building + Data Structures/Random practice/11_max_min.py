# Take 3 numbers and print largest (no max() allowed)

num = [int(x) for x in input("Enter numbers seperated by commas: ").split(",")]
print(num)

minimum = num[0]
maximum = num[0]

for i in num:
    if i<minimum:
        minimum = i
    if i>maximum:
        maximum = i
    
print("Minimum: ",minimum)
print("Maximum: ",maximum)