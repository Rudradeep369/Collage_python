
# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125


def print_table(rows):
    
    for n in range(1, rows + 1):
        row = [n, n**0, n**1, n**2, n**3]
        print(" ".join(map(str, row)))

rows = int(input("Enter number : "))
print_table(rows)

# Output

# Enter number : 5
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125