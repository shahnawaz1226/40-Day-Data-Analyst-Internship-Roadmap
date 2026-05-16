'''
Names + marks given
Second lowest marks nikaalne hain
Phir us marks wale students ke names
Output alphabetical order me

Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output
Berry
Harry
'''

students = []

n = int(input())

# Take input
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# Get all unique scores
scores = []
for student in students:
    scores.append(student[1])

unique_scores = sorted(set(scores))

# Second lowest score
second_lowest = unique_scores[1]

# Get names with second lowest score
result = []
for student in students:
    if student[1] == second_lowest:
        result.append(student[0])

# Print names in alphabetical order
for name in sorted(result):
    print(name)

