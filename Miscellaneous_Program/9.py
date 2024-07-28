# Write a python program to check whether a number is palindrome or not.


def is_palindrome_native(num):
    return str(num) == str(num)[::-1]

number = int(input("Enter number: "))
if is_palindrome_native(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# Output

# Enter number: 121
# 121 is a palindrome.