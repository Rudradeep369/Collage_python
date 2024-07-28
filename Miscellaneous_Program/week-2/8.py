# Write a python program to calculate the exponential of a number.

base = int(input("Enter 1st number: "))
exponent = int(input("Enter 2nd number: "))

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))

# Output

# Enter 1st number: 3
# Enter 2nd number: 4
# Answer = 81