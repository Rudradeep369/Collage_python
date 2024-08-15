# Write a program to enter a string. Calculate the length of the string. Find the substring country.
# Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.


sentence = input("Enter a sentence: ")
letter_count = len(sentence)
print("Number of letters:", letter_count)

if "country" in sentence:
    print("The word 'country' is in the sentence.")

word_count = {}
words = sentence.split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word counts:")
for word, count in word_count.items():
    print(word, ":", count)



# Output

# Enter a sentence: India is my motherland. I love my country. Capital of India is New Delhi.
# Number of letters: 73
# The word 'country' is in the sentence.
# Word counts:
# India : 2
# is : 2
# my : 2
# motherland. : 1
# I : 1
# love : 1
# country. : 1
# Capital : 1
# of : 1
# New : 1
# Delhi. : 1