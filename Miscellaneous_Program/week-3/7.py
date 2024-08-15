# Reverse the elements in an array of integers without using a second array

import numpy as np

n=int(input("Enter number : "))

arr=np.zeros((n),dtype=int)

for i in range(n):
    arr[i]=int(input("Enter Elements : "))

print(arr)

print("Reversed Array : ",arr[::-1])

# Output

# Enter number : 4
# Enter Elements : 1
# Enter Elements : 2
# Enter Elements : 3
# Enter Elements : 4
# [1 2 3 4]
# Reversed Array :  [4 3 2 1]