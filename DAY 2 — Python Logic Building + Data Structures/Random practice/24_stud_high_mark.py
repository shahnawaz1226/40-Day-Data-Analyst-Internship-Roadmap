# Create a dictionary of 5 students:
# name → marks
# Print student with highest marks

stud = {
"Shahnawaz": 99.9,
"Abdullah": 100,
"Rishab": 85,
"Lakshya": 70,
"Vyom": 90
}
keys = stud.keys()
vals = stud.values()
# topper = max(stud, key=stud.get)
# print(topper,":",stud.get(topper))
topper = 0
name = ""

for keys, vals in stud.items():
    if vals>topper:
        topper=vals
        name = keys
print(name, topper)


# Another method ------------------------------------------------------------------------------->
# Another method by taking input
students = {}

# Input 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find student with highest marks
topper = max(students, key=students.get)

print("Student with highest marks:")
print(topper, "→", students[topper])

# Another method ------------------------------------------------------------------------------->
highest_marks = 0
topper = ""

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        topper = name

print(topper, "→", highest_marks)
