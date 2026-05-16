# Reverse a Number
# Take a number like 12345 and print it reversed: 54321.

number = int(input("Enter number: "))
rev_num =0
while number >0:
    digit = number%10
    rev_num = rev_num* 10 + digit 
    number = number//10
print(rev_num)

# def reverse(number, rev_num = 0):
#     if number==0:
#         return rev_num
#     else:
#         return reverse(number//10, rev_num*10 + number%10)
# print(reverse(number))