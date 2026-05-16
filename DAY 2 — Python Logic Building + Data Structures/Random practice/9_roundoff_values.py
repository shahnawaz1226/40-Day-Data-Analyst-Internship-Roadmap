'''Input a float number and print:
rounded value
integer part only'''

n = float(input("Enter number: "))
print(round(n))

'''
Method 	Python Code	Result for 47.6	Description
round()	round(47.6)	48	Rounds to the nearest whole number.
int()	int(47.6)	47	Discards the decimal part (truncates).
math.floor()	math.floor(47.6)	47	Rounds down to the nearest integer.
math.ceil()	math.ceil(47.6)	48	Rounds up to the nearest integer.
'''