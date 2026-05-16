'''
Grade Predictor
Marks input (0–100):
90+ → A
75–89 → B
50–74 → C
<50 → Fail
'''

marks = float(input("Enter you marks(0-100): "))

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")
