'''
Even – Odd + Sign Detector
User ek number de:
even / odd
positive / negative / zero
Sab ek hi program me.
'''
num = int(input("Enter number: "))
if num%2==0 and num>0:
    print(f"{num} is even")
    print(f"{num} is positive")
elif num==0:
    print(f"{num} is zero")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is odd")
    print(f"{num} is positive")

