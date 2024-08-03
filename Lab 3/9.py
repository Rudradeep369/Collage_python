# Print the pattern upto N Lines:

# .
# /_\
# .
# / \
# /___\
# .
# / \
# / \
# /_____\

# N=2 N=3 N=4


def print_pattern(N):

    print(" " * (N - 1) + ".")
    for i in range(1, N):
        print(" " * (N - i - 1) + "/" + " " * (2 * i - 1) + "\\")

    if N > 1:
        print("/" + "_" * (2 * N - 2) + "\\")

N = int(input("Enter the number of lines N: "))
print_pattern(N)

# Output

# Enter the number of lines N: 4
#    .
#   / \
#  /   \
# /     \
# /______\
