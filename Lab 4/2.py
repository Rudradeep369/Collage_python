# 2.Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


def sort_words(words_string):

  words = words_string.split(',')
  words.sort()
  sorted_words = ','.join(words)
  print(sorted_words)

input_string = input("Enter comma-separated words: ")

sort_words(input_string)

# Output

# Enter comma-separated words: without,hello,bag,world
# bag,hello,without,world