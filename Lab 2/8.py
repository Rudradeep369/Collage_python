# Write a function to calculate the power of a number using recursion

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} to the power of {exp} is: {result}")

# Output

# Enter the base number: 4
# Enter the exponent: 8
# 4 to the power of 8 is: 65536