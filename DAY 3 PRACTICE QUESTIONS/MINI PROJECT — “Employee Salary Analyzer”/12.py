# BONUS CHALLENGE 🔥
# Create a NumPy array from 1–100.

# Then:
# print only even numbers
# print numbers divisible by 7
# print squares of all numbers

import numpy as np

arr  = np.arange(1,101)

print("Evens:", arr[arr%2==0])
print("Divisible by 7:", arr[arr%7==0])
print("Squares of all natural number from 1 to 100:", arr**2)


# TODAY’S INTERVIEW QUESTIONS
# Prepare answers:

# 1.
# Why NumPy faster than Python lists?

# 2.
# Difference between list and NumPy array?

# 3.
# Why arrays useful in analytics?

# 4.
# What is vectorized operation?



# 1. Why is NumPy faster than Python lists?

# NumPy faster hota hai because:

# It stores data in continuous memory.
# NumPy internally C language use karta hai.
# Loops Python ki jagah optimized low-level code me run hote hain.
# Practical Example:
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr * 2)

# Ye operation NumPy me bahut fast hota hai compared to normal Python loops.

# Interview Line:

# “NumPy optimized C implementation aur continuous memory allocation ki wajah se Python lists se faster hota hai.”

# 2. Difference between List and NumPy Array?
# List	NumPy Array
# Different data types store kar sakta hai	Mostly same data type
# Slower	Faster
# Mathematical operations difficult	Easy and optimized
# More memory use	Less memory use
# Practical Example:
# # Python List
# a = [1, 2, 3]
# # a * 2 => [1,2,3,1,2,3]

# # NumPy Array
# import numpy as np
# b = np.array([1, 2, 3])

# print(b * 2)  # [2 4 6]
# Interview Line:

# “NumPy arrays numerical computations aur analytics tasks ke liye optimized hote hain, jabki lists general-purpose data storage ke liye.”

# 3. Why are arrays useful in analytics?

# Arrays useful hote hain because:

# Large numerical data efficiently handle karte hain.
# Fast calculations possible hoti hain.
# Data cleaning, filtering, statistics, ML sab easy ho jata hai.
# Practical Example:
# import numpy as np

# sales = np.array([200, 300, 400])

# print(np.mean(sales))
# Interview Line:

# “Analytics me arrays fast computation aur bulk data processing ke liye bahut useful hote hain.”

# 4. What is Vectorized Operation?

# Vectorized operation ka matlab:
# Loop likhe bina entire array par operation perform karna.

# Practical Example:
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr + 10)

# Output:

# [11 12 13 14]

# Yaha manually loop nahi likha.

# Interview Line:

# “Vectorized operations NumPy me loop-free fast computations provide karte hain, jo performance improve karte hain.”

# Mini hack for interview 🧠
# Agar interviewer NumPy pe deep pooche:

# “NumPy is mainly used for fast numerical computing and handling large-scale analytical data efficiently.”

# Bas ye line kaafi impact deti hai.