# Write a python program to count the number of digits of an integer.

num = int(input("Enter 1st number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))

# Output

# Enter 1st number: 3452
# Number of digits: 4