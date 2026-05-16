# Create a tuple of 5 elements and:
# print first & last element
# count duplicates of number

data = tuple(map(int, input("Enter elements seperated by spaces: ").split()))
print(data[0])
print(data[-1])
uniq = []

for num in data:
    if num not in uniq:
        uniq.append(num)

print(len(data)- len(uniq))