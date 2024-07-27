# Write a Python program that prompts the user to enter a base number and an exponent,
# and then calculates the power of the base to the exponent. The program should not use the
# exponentiation operator (**) or the math.pow() function.

def calculate_power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = calculate_power(base, exp)
print(f"{base} to the power of {exp} is: {result}")

# Output

# Enter the base number: 2
# Enter the exponent: 10
# 2 to the power of 10 is: 1024