# Write a program which makes use of function to display all such numbers which are
# divisible by 7 but are not a multiple of 5, between 1000 and 2000.

n1=1000
n2=2000

for i in range(n1,n2+1):
    if (i % 2 != 0) and (i % 7 ==0) and (i % 5 != 0):
        print(i)