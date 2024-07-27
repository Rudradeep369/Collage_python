# To solve the quadratic equation.

import cmath

def solve_quadratic(n1, n2, n3):
    discriminant = cmath.sqrt(n2**2 - 4*n1*n3)
    
    x1 = (-n2 + discriminant) / (2 * n1)
    x2 = (-n2 - discriminant) / (2 * n1)
    
    return x1, x2


n1=float(input("Enter 1 number :"))
n2=float(input("Enter 2 number :"))
n3=float(input("Enter 3 number :"))

s1, s2 = solve_quadratic(n1, n2, n3)

print(f"The solutions are {s1} and {s2}")

# OutPut

# Enter 1 number :1
# Enter 2 number :5
# Enter 3 number :6
# The solutions are (-2+0j) and (-3+0j)