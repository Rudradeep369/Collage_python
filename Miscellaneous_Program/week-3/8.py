# Write a program to enter n elements in an array and find smallest number among them

import numpy as np

n=int(input("Enter number : "))

arr=np.zeros((n),dtype=int)

for i in range(n):
    arr[i]=int(input("Enter Elements : "))

arr.sort()

print("Smallest element : ",arr[0])

# Output

# Enter number : 4
# Enter Elements : 1
# Enter Elements : 2
# Enter Elements : 3
# Enter Elements : 4
# Smallest element :  1