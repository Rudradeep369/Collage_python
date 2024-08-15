# 6. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or
# "Yes", otherwise print "No".

user_input = input("Enter a string: ")
if user_input.lower() == "yes":
    print("Yes")
else:
    print("No")

# Output

# Enter a string: YES
# Yes