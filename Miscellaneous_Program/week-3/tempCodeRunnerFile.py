import numpy as np

n1=int(input("Enter row : "))
n2=int(input("Enter column : "))

arr=np.zeros((n1,n2),dtype=int)

for i in range(n1):
    for j in (n2):
        arr[i,j]=int(input("Enter elements : "))

print(arr)