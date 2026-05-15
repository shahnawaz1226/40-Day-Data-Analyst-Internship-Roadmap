# Mini Task (Important)

# Create a:

# “Student Marks Analyzer”

# Features:

# Take student marks list
# Calculate:
# average
# highest
# lowest
# Print pass/fail count

student_marks = [45, 97, 56, 46, 87, 56, 97, 66, 86, 87, 32, 33, 31, 31, 33]

#Average
sum_marks = 0
for i in student_marks:
    sum_marks+=i
print("Average marks: ", (sum_marks/len(student_marks)))

# print(sum(student_marks)/len(student_marks))

#Highest
# student_marks.sort()
# print(student_marks[-1])

highest_mark = student_marks[0]
for i in student_marks:
    if i>highest_mark:
        highest_mark = i
print("Highest: ", highest_mark)

#Lowest
# student_marks.sort()
# print(student_marks[0])

lowest_mark = student_marks[0]
for i in student_marks:
    if i<lowest_mark:
        lowest_mark = i
print("Lowest: ", lowest_mark)


#Pass Fail count
Pass = 0
Fail = 0

for i in student_marks:
    if i<33:
        Fail+=1
    else:
        Pass+=1
print("No. of pass students: ", Pass)
print("No. of Fail students: ", Fail)



# Real-World Analyst Thinking Task

# Imagine:
# You are analyzing marks of students in a coaching institute.

# Answer:

# Which metric is most important?
# What insights can school owner get?
# What chart would you use later for visualization?

# Think like analyst. Not coder.