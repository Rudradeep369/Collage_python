# Compute a)sin of 60 degree b)cos of pi c)sin(0.8660254037844386) d)tan of 90 degree

import math  

a = math.sin(math.radians(60))  

b = math.cos(math.pi)  

c = math.sin(0.8660254037844386) 

try:
    d = math.tan(math.radians(90))  
except ValueError:
    d = "undefined (approaches infinity)" 

print(f"Sine of 60 degrees: {a}")
print(f"Cosine of π: {b}")
print(f"Sine of 0.8660254037844386: {c}")
print(f"Tangent of 90 degrees: {d}")


# Output

# Sine of 60 degrees: 0.8660254037844386
# Cosine of π: -1.0
# Sine of 0.8660254037844386: 0.7617599814162892
# Tangent of 90 degrees: 1.633123935319537e+16  