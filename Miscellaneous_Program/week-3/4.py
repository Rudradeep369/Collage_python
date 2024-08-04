#   program to search an element in an array

import numpy as np

n=int(input("Enter Number : "))

arr=np.zeros((n),dtype=int)

for i in range(n):
    arr[i]=int(input("Enter Elements {}: ".format(i+1)))

print(arr)

search=int(input("Enter Element to search : "))

if search in arr:
    s = np.where(arr==search)
    print(s)
else:
    print("Error")

# Output:
# Enter Number : 2
# Enter Elements 1: 1
# Enter Elements 2: 2
# [1 2]
# Enter Element to search : 2
# (array([1]),)