# program to find the range of a 1D array

import numpy as np

n=int(input("Enter number : "))

arr=np.zeros((n),dtype=int)

for i in range(n):
    arr[i]=int(input("Enter Elements : "))

print(arr)
print("Range : ",len(arr))

# Output

# Enter number : 4
# Enter Elements : 1
# Enter Elements : 2
# Enter Elements : 3
# Enter Elements : 4
# [1 2 3 4] 
# Range :  4