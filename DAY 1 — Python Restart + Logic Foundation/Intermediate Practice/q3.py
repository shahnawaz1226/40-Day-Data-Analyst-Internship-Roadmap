# 3. For Loops
# Print numbers from 1 to 10 using a for loop.
# Print the multiplication table of a number (entered by user).
# Calculate the sum of all numbers from 1 to 100 using a for loop.
# Print the following pattern using a for loop:
# *
# **
# ***
# ****


# 1
# for i in range(1,11):
#     print(i)

# 2
num = int(input("Enter number: "))
for i in range(1,11):
    print(i*num)

# 3
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 4
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    # print("*"*i)
    # print(" "* (rows-i), "*"*i)
    print(" "* (rows-i), "*"* (2*i-1))