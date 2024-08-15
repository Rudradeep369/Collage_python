# Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


def remove_duplicates_and_sort(words):

  unique_words = list(set(words.split()))
  unique_words.sort()
  return unique_words

if __name__ == "__main__":
  input_string = input("Enter whitespace separated words: ")
  sorted_words = remove_duplicates_and_sort(input_string)
  print(" ".join(sorted_words))


# Output

# Enter whitespace separated words: hello world and practice makes perfect and hello world again
# again and hello makes perfect practice world  