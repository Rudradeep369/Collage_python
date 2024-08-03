# Print the pattern upto N lines:

# 1 2
# 4 3

# 1 2 3
# 8 9 4
# 7 6 5

# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

#  N=2 N=3 N=4


def print_spiral_pattern(N):
    matrix = [[0] * N for _ in range(N)]
    
    num = 1
    left, right = 0, N - 1
    top, bottom = 0, N - 1
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
 
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    

    for row in matrix:
        print(' '.join(map(str, row)))


N = int(input("Enter the number of lines N: "))
print_spiral_pattern(N)

# Output

# Enter the number of lines N: 4
# 1 2 3 4   
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7  