# Write program to find the sum of all odd numbers in a 2D array

import numpy as np

row=int(input("Enter row : "))
col=int(input("Enter column : "))

arr=np.zeros((row,col),dtype=int)

for i in range(row):
    for j in range(col):
        arr[i,j]=int(input("Enter elements {} : ".format(i+1,j+1)))

print(arr)

odd_sum=0

for i in range(row):
    for j in range(col):
        if arr[i,j] % 2 != 0:
            odd_sum+=arr[i,j]

print("Odd_sum : ",odd_sum)

# Output

# Enter row : 2
# Enter column : 2
# Enter elements 1 : 1
# Enter elements 1 : 2
# Enter elements 2 : 3
# Enter elements 2 : 4
# [[1 2]      
#  [3 4]]     
# Odd_sum :  4