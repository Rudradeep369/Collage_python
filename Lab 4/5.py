# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def count_letters_and_digits(sentence):
  letters = 0
  digits = 0
  for char in sentence:
    if char.isalpha():
      letters += 1
    elif char.isdigit():
      digits += 1
  return letters, digits

sentence = input("Enter a sentence: ")

letters, digits = count_letters_and_digits(sentence)

print("LETTERS", letters)
print("DIGITS", digits)

# Output

# Enter a sentence: hello world! 123
# LETTERS 10
# DIGITS 3  