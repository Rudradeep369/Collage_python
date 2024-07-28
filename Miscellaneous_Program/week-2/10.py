# Write a python program to check whether a number is prime or not.

num = int(input("Enter number: "))
if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Output

# Enter number: 11
# 11 is a prime number