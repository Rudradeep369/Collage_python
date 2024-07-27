# Write a Python program to print the first 6 terms of a geometric sequence starting with 2
# and having a common ratio of 3.

def geometric_sequence(a, r, n):
    for i in range(n):
        print(a * (r ** i))

a = 2 
r = 3 
n = 6  
geometric_sequence(a, r, n)

# Output

# 2
# 6
# 18
# 54
# 162
# 486