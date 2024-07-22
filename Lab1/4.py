# WAP to display reverse of a number

n=int(input("Enter number : "))

num=n
r=0

while n>0:
    temp=n%10
    r=r*10+temp
    n=n//10
print(r)