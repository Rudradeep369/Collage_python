# Write a program in Python to check if a number is Krishnamurthy number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_krishnamurthy(n):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(n))
    return sum_of_factorials == n

number = int(input("Enter a number: "))
if is_krishnamurthy(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")


# Output

# Enter a number: 389328932
# 389328932 is not a Krishnamurthy number.