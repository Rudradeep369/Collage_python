# Write a program to print transpose of matrix

import numpy as np

row=int(input("Enter Row : "))
col=int(input("Enter Column : "))

arr=np.zeros((row,col),dtype=int)

for i in range(row):
    for j in range(col):
        arr[i,j]=int(input("Enter Elements {}: ".format(i+1)))

print(arr)
print("Transpose")
print(arr.T)

# Output

# Enter Row : 2
# Enter Column : 2
# Enter Elements 1: 1
# Enter Elements 1: 2
# Enter Elements 2: 3
# Enter Elements 2: 4
# [[1 2]   
#  [3 4]]  
# Transpose
# [[1 3]   
#  [2 4]]  