# Multiplication Table
# Print the multiplication table for any number the user enters (1 to 10).

n = int(input("Enter table number: "))

for i in range(1,11):
    num = n*i
    print(num)

# # Get input from the user
# num = int(input("Enter a number (1-10): "))

# print(f"Multiplication Table for {num}:")

# # Loop from 1 to 10 and print the table
# for i in range(1, 11):  # range(1, 11) generates numbers 1, 2, ..., 10
#     print(f"{num} * {i} = {num * i}")
