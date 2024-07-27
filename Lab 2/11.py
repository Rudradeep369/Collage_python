# Write a program in Python to find the sum of digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = int(input("Enter a number: "))
sum_digits = sum_of_digits(number)
print(f"Sum of digits: {sum_digits}")


# Output

# Enter a number: 55
# Sum of digits: 10