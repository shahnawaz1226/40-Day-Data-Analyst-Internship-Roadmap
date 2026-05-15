# SECTION B — Dictionaries
# Q6
# Create dictionary of student marks.
# Print:
# highest marks
# lowest marks
# average marks

student_marks = {
    "Ali": 85,
    "Sara": 92,
    "John": 78,
    "Emma": 95,
    "Mike": 88
}

print("Highest marks:", max(student_marks.values()))
print("Lowest marks:", min(student_marks.values()))
print("Average marks:", sum(student_marks.values())/len(student_marks))