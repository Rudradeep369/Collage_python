#  Declare a function named print_list. It takes a list as a parameter and it prints out each
# element of the list.

def print_list(my_list):

  for item in my_list:
    print(item)

num = int(input("Enter no.of elements: "))
my_list = []
for i in range(num):
  element = int(input(f"Enter element {i+1}: "))
  my_list.append(element)

print_list(my_list)

# Output

# Enter no.of elements: 5
# Enter element 1: 1
# Enter element 2: 2
# Enter element 3: 3
# Enter element 4: 4
# Enter element 5: 5
# 1
# 2
# 3
# 4
# 5