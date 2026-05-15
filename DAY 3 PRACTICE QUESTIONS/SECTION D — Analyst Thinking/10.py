# Q10
# Find days where sales > average sales.

import numpy as np

sales = np.array([2000, 3400, 2800, 4100, 3900])

print(sales[sales > np.mean(sales)])