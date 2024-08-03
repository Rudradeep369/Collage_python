# Write a Python program to find all roots of a quadratic equation.

import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
d = (b**2) - (4*a*c)  
  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))  

# Output

# Enter a: 5
# Enter b: 8
# Enter c: 1
# The solution are (-1.4633249580710799+0j) and (-0.13667504192892005+0j)