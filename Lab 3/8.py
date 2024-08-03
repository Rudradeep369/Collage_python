# Write a program to compute cosine of x. The user should supply x and a positive integer n.
# We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# cos x = 1 - x2/2! + x4/4! - x6/6! ....  


import math
\
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = float(input("Enter the value of x : "))
n = int(input("Enter the number of terms n: "))

cos_x = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    cos_x += term

print(f"The computed value of cos({x}) using {n} terms is: {cos_x}")

# Output

# Enter the value of x : 2
# Enter the number of terms n: 4
# The computed value of cos(2.0) using 4 terms is: -0.4222222222222223