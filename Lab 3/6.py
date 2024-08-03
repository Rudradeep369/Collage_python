#  Compute the sum up to n terms in the series
# 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.

def sum(n):
    i=1
    s=0.0

    for i in range(1,n+1):
        s=s+1/i
    return s

n=int(input("Enter number : "))
print("Answer : ",round(sum(n),2))

# Output

# Enter number : 10
# Answer :  2.93