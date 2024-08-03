# Write a program to compute sin x for given x. The user should supply x and a positive integer
# n. We compute the sine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = float(input("Enter the value of x : "))
n = int(input("Enter the number of terms n: "))

sin_x = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    sin_x += term

print(f"The computed value of sin({x}) using {n} terms is: {sin_x}")

# Output

# Enter the value of x : 2
# Enter the number of terms n: 4
# The computed value of sin(2.0) using 4 terms is: 0.9079365079365079
