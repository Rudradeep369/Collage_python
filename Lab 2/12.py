#  Write a program in Python that prompts the user to input a number and prints its
# multiplication table.

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number: "))
multiplication_table(number)

# Output

# Enter a number: 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20