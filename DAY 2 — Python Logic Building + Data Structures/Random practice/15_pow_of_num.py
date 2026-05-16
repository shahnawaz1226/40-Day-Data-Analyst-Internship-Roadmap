# Power of a Number: Compute \(a^{b}\) (e.g., \(2^{3}=8\)) by multiplying \(a\) by itself \(b\) times.

def power(a,b):
    if a==0:
        return 0
    elif b==0:
        return 1
    return a*power(a,b-1)

a = int(input("Enter (base): "))
b = int(input("Enter (power): "))
print(power(a,b))

# a = int(input("Enter (base): "))
# b = int(input("Enter (power): "))
# result = 1
# for i in range(b):
#     result*=a

# print(result)