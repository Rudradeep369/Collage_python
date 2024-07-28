# Write a python program to find HCF of two Numbers

def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("The H.C.F. is", compute_hcf(num1, num2))

# Output

# Enter 1st number: 54
# Enter 2nd number: 24
# The H.C.F. is 6