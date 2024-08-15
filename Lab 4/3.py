# Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


def capitalize_lines(lines):

  for line in lines:
    print(line.upper())

input_lines = []
for _ in range(1):
  line = input("Enter String : ")
  input_lines.append(line)

print("Output")
capitalize_lines(input_lines)

# output

# Enter String : Practice makes perfect
# Output
# PRACTICE MAKES PERFECT