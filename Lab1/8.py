# WAP to check whether a number is a palindrome or not

n=int(input("Enter number : "))
num=n
r=0

while n>0:
    temp=n%10
    r=r*10+temp
    n=n//10

if num==r:
    print("Palindrom")
else:
    print("Not")