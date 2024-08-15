# 8. Please write a program which count and print the numbers of each character in a string input by
# console.
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

def count_characters(string):

  char_count = {}
  for char in string:
    char_count[char] = char_count.get(char, 0) + 1
  return char_count

input_string = input("Enter a string: ")

char_counts = count_characters(input_string)

for char, count in char_counts.items():
  print(char, count, sep=",")


# Output

# Enter a string: abcdefgabc
# a,2
# b,2
# c,2
# d,1
# e,1
# f,1
# g,1