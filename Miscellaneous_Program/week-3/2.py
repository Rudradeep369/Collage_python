# Write a python program to calculate Sum of two 2-dimensional arrays.


import numpy as np

n1=int(input("Enter row : "))
n2=int(input("Enter column : "))

arr = np.zeros((n1, n2), dtype=int)

for i in range(n1):
    for j in range(n2):
        arr[i,j]=int(input("Enter elements : "))

print(arr)
print("Sum : ",arr.sum())

# output

# Enter row : 2
# Enter column : 3
# Enter elements : 1
# Enter elements : 2
# Enter elements : 3
# Enter elements : 4
# Enter elements : 5
# Enter elements : 6
# [[1 2 3] 
#  [4 5 6]]
# Sum :  21
