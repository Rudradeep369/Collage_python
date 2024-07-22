#  WAP to generate prime number series up to n

n=int(input("Enter number "))

for i in range(2,n+1):
    if i % 2 == 0:
        print(i)