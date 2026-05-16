'''Password Strength Checker 🔐

Take input user password:
Check:
length ≥ 8
at least 1 digit
at least 1 uppercase
Final output:
“Strong” / “Weak” with reason
'''

password = input("Enter your password: ")

has_digit = False
has_upper = False

# Check each character
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

# Conditions
if len(password) < 8:
    print("Weak: Password length should be at least 8 characters")

elif not has_digit:
    print("Weak: Password must contain at least one digit")

elif not has_upper:
    print("Weak: Password must contain at least one uppercase letter")

else:
    print("Strong: Password is secure 💪")



