# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
# input number of participant's and then scores of participants
# find the score of runner-up

n = int(input("Enter no. of participants: "))
scores = map(int, input("Enter scores seperated by space: ").split())

unq_scores = list(set(scores))
unq_scores.sort()
print("Runner-up score: ", unq_scores[-2])

