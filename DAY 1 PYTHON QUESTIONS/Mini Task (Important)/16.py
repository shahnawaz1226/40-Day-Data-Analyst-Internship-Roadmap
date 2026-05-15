# Day 1 Bonus Challenge
# FizzBuzz

# From 1–100:

# divisible by 3 → Fizz
# divisible by 5 → Buzz
# both → FizzBuzz

# Classic logic test. Interviews LOVE this.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    