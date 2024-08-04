# Write a program to calculate Sum & Average of an integer array.

def sum_avg(num):
 
  total = sum(num)
  average = total / len(num)
  return total, average

n = int(input("Enter the number of elements: "))
num = []
for i in range(n):
  number = int(input("Enter element {}: ".format(i + 1)))
  num.append(number)

total, average = sum_avg(num)

print("Sum:", total)
print("Average:", average)

# Output

# Enter the number of elements: 4
# Enter element 1: 1
# Enter element 2: 2
# Enter element 3: 3
# Enter element 4: 4
# Sum: 10
# Average: 2.5