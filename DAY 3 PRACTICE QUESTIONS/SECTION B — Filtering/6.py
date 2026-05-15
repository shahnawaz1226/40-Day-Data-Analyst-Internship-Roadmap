# Q6
# Print numbers divisible by 5.

import numpy as np
arr = np.array([23, 67, 12, 89, 54, 43])

print(arr[arr%5==0])