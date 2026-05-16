'''Number Analyzer

User ek list de (comma separated).
Find:
max
min
sum
average

No built-in shortcut like sum() allowed 🚫
'''

# User input: converting string input into a list of numbers
data = [float(x) for x in input("Enter numbers separated by comma: ").split(",")]

if not data:
    print("The list is empty.")
else:
    # Initialize variables using the first element
    total_sum = 0
    maximum = data[0]
    minimum = data[0]
    count = 0

    for num in data:
        total_sum += num
        count += 1
        
        if num > maximum:
            maximum = num
            
        if num < minimum:
            minimum = num

    average = total_sum / count

    print(f"Sum: {total_sum}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Average: {average}")
