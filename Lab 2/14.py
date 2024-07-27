# Print the series upto N terms: 1,2,6,24,120,720 …

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_series(n):
    for i in range(1, n + 1):
        print(factorial(i), end=", ")

terms = int(input("Enter the number of terms: "))
print_series(terms)

# Output

# Enter the number of terms: 5
# 1, 2, 6, 24, 120, 