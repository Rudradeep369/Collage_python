# Write a Java program to calculate the sum of natural numbers up to a certain range.

# Sum of natural numbers up to num

num = int(input("Enter number : "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

# Output

# Enter number : 16
# The sum is 136