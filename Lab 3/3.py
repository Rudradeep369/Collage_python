#  Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which
# calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

def solve_quadratic_eqn(a, b, c, x):

  result = a * (x**2) + b * x + c
  return result

print("Quadratic Equation: ax² + bx + c = 0")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
x = int(input("\nEnter x: "))

result = solve_quadratic_eqn(a, b, c, x)
print("The value of the equation for x =", x, "is:", result)

# Output

# Quadratic Equation: ax² + bx + c = 0
# Enter a: 2
# Enter b: 4
# Enter c: 5

# Enter x: 2
# The value of the equation for x = 2 is: 21