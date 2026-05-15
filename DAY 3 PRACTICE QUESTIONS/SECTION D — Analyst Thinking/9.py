# Q9
# You have sales data:

# sales = np.array([2000, 3400, 2800, 4100, 3900])

# Find:
# total sales
# average sales
# highest sales
# lowest sales

import numpy as np

sales = np.array([2000, 3400, 2800, 4100, 3900])

print("Total sales:", np.sum(sales))
print("Average sales:", np.mean(sales))
print("Highest sale:", np.max(sales))
print("Lowest sale:", np.min(sales))