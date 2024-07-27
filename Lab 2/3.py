# Find GCD of two numbers

n1=int(input("Enter 1 number :"))
n2=int(input("Enter 2 number :"))

while n1 != n2:
    if n1>n2:
        n1-=n2
    else:
        n2-=n1

print(n1)

# Output 

# Enter 1 number :36
# Enter 2 number :60
# 12