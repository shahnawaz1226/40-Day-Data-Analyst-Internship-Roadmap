# “Daily Sales Analyzer”
# Create program using dictionary.

# Example:
# sales = {
#     "Monday": 2000,
#     "Tuesday": 3400,
#     "Wednesday": 2800,
#     "Thursday": 4100,
#     "Friday": 3900
# }

# Program should:
# calculate total sales
# average sales
# highest sales day
# lowest sales day

sales = {
    "Monday": 2000,
    "Tuesday": 3400,
    "Wednesday": 2800,
    "Thursday": 4100,
    "Friday": 3900
}

print("Total Sales: ", sum(sales.values()))
print("Average Sales: ", sum(sales.values())/len(sales))
print("Highest Sales day: ", max(sales, key=sales.get))
print("Lowest Sales day: ", min(sales, key=sales.get))


# ANALYST THINKING TASK

# Imagine:
# You work in e-commerce company.

# Question:

# Why would average sales alone be misleading?
# Why highest sales day important?
# Which chart would best visualize daily sales?

# Think business-wise.