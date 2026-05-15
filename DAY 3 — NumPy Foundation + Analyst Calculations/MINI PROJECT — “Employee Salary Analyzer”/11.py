# Dataset:
# salaries = np.array([25000, 32000, 28000, 41000, 36000, 29000])

# Tasks:
# average salary
# highest salary
# lowest salary
# salaries above average
# increase all salaries by 10%
# print updated salaries

import numpy as np

salaries = np.array([25000, 32000, 28000, 41000, 36000, 29000])

print("Average salary:", np.mean(salaries))
print("Highest salary:", np.max(salaries))
print("Lowest salary:", np.min(salaries))
print("Above Average salary:", salaries[salaries>np.mean(salaries)])
print("Salary bonus +10%:", salaries + salaries*(10/100))


# IMPORTANT ANALYST CONCEPT
# Why NumPy Matters Before Pandas?

# Because:
# Pandas internally works using NumPy.

# If NumPy weak:
# Pandas confusing lagega.

# Strong NumPy = smoother future.