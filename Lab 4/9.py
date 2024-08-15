# 9.Write a program that accepts a string
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence


def string_operations(string):

  reversed_string = string[::-1]
  is_palindrome = reversed_string == string
  substring = "rudra" 
  ends_with_substring = string.endswith(substring)
  capitalized_string = ' '.join(word.capitalize() for word in string.split())

  anagram_string = "deep"  
  is_anagram = sorted(string) == sorted(anagram_string)
  vowels = 'aeiouAEIOU'
  no_vowels_string = ''.join(char for char in string if char not in vowels)
  longest_word = max(string.split(), key=len)
  longest_word_length = len(longest_word)

  return {
      "reversed_string": reversed_string,
      "is_palindrome": is_palindrome,
      "ends_with_substring": ends_with_substring,
      "capitalized_string": capitalized_string,
      "is_anagram": is_anagram,
      "no_vowels_string": no_vowels_string,
      "longest_word_length": longest_word_length
  }

if __name__ == "__main__":
  string = input("Enter a string: ")
  results = string_operations(string)
  print("Reversed string:", results["reversed_string"])
  print("Is palindrome:", results["is_palindrome"])
  print("Ends with 'rudra':", results["ends_with_substring"])
  print("Capitalized string:", results["capitalized_string"])
  print("Is anagram of 'deep':", results["is_anagram"])
  print("String without vowels:", results["no_vowels_string"])
  print("Length of longest word:", results["longest_word_length"])


# Output

# Enter a string: hello world and practice makes perfect
# Reversed string: tcefrep sekam ecitcarp dna dlrow olleh   
# Is palindrome: False
# Ends with 'rudra': False
# Capitalized string: Hello World And Practice Makes Perfect
# Is anagram of 'deep': False
# String without vowels: hll wrld nd prctc mks prfct        
# Length of longest word: 8