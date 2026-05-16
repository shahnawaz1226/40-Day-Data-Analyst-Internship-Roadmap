# Simple Interest Calculator
# Calculate simple interest given principal, rate, and time.

# rate = (5/100)*100
rate = 5
time = 5

principal = int(input("Enter principal amount: "))

def s_i(principal):
    return (principal*rate*time)/100

print(s_i(principal))