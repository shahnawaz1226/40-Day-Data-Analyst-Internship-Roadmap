# 4. While Loops
# Print numbers from 1 to 10 using a while loop.
# Write a program that keeps asking the user to enter a password until they enter the correct one.
# Use a while loop to reverse a given number (e.g., 123 → 321).

# 1
i = 1
while i<=10:
    print(i)
    i += 1


# 2
password = input("Enter password: ")
pswrd = "python123"

while password != pswrd:
    print("Wrong! Try Again!")
    break

if password == pswrd:
    print("Access Granted.")

# 3
n = int(input("Enter number: "))
# print(n[::-1])
print(str(n)[::-1])