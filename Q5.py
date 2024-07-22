# WAP to find factors of a given number

n=int(input("Enter Number : "))

factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print ("Factors of {} = {}".format(n,factors))