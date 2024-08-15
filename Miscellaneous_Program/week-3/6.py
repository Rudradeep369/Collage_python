#  program to find the sum of diagonal elements in a 2D array

import numpy as np

n1=int(input("Enter row : "))
n2=int(input("Enter column : "))

arr = np.zeros((n1, n2), dtype=int)

for i in range(n1):
    for j in range(n2):
        arr[i,j]=int(input("Enter elements : "))

print(arr)

for i in range(n1):
    for j in range(n2):
        if i==j:
            print(arr[i,j],end=' , ')

# output

# Enter row : 2
# Enter column : 2
# Enter elements : 1
# Enter elements : 2
# Enter elements : 3
# Enter elements : 4
# [[1 2]  
#  [3 4]] 
# 1 , 4 , 