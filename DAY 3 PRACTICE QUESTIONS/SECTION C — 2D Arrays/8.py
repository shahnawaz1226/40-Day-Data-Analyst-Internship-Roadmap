# Q8
# Find row-wise sums.

import numpy as np

arr = np.array([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
])

print(arr.sum(axis=1)) #axis=0 for columns