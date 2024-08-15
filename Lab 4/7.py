# 7. Write a program which accepts a sequence of words separated by whitespace as input to print the
# words composed of digits only.
# Example:
# If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# In case of input data being supplied to the question, it should be assumed to be a console input.



def extract_digits(input_string):

  words = input_string.split()
  digits = [word for word in words if word.isdigit()]
  return digits

input_string = input("Enter whitespace separated words: ")

digit_list = extract_digits(input_string)
print(digit_list)

# Output 

# Enter whitespace separated words: 2 cats and 3 dogs.
# ['2', '3']