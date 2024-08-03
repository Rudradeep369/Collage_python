#  Declare a function named reverse_list. It takes an array as a parameter and it returns the
# reverse of the array (use loops).

import numpy as np

def reverse_list(arr):

  reversed_arr = arr[::-1]
  print(reversed_arr)

n = int(input("Enter the number of elements: "))
arr = np.empty(n, dtype=int)

for i in range(n):
  arr[i] = int(input(f"Enter element {i+1}: "))

reverse_list(arr)

# Output

# Enter the number of elements: 4
# Enter element 1: 1
# Enter element 2: 2
# Enter element 3: 3
# Enter element 4: 4
# [4 3 2 1]