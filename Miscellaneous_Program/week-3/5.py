#   program to find the sum of even numbers in an integer array

import numpy as np

n=int(input("Enter number : "))

arr=np.zeros((n),dtype=int)

for i in range(n):
    arr[i]=int(input("Enter Elements {}: ".format(i+1)))

print(arr)

sum_elements=arr[arr % 2 == 0]

if sum_elements.size == 0:
    print("none")
else:
    print("Sum of even numbers : ",sum_elements.sum())

# output

# Enter number : 4
# Enter Elements 1: 1
# Enter Elements 2: 2
# Enter Elements 3: 3
# Enter Elements 4: 4
# [1 2 3 4]
# Sum of even numbers :  6