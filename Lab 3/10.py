# Print a number as a 8 segment display N Lines:

#    _
#    _|
#    |_
#    _
#    _|
#    _|
#    |_|
#    |
# N=2 N=3 N=4


def print_8_segment(num):
  
    segments = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }
    
    num_str = str(num)
    
    display_lines = ["", "", ""]
    
    for digit in num_str:
        for i in range(3):
            display_lines[i] += segments[digit][i] + " "
    
    for line in display_lines:
        print(line)

N = int(input("Enter the number of lines N: "))

print_8_segment(N)

# Output

# Enter the number of lines N: 4
    
# |_| 
#   | 