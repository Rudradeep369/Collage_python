#  Write a function called calculate_slope which return the slope of a linear equation

x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

def calculate_slope():
    if x2-x1==0:
        slope = (y2 - y1) / (x2 - x1)
        print("The slope is:", slope)
    else:
        print("The line is vertical.")
    
calculate_slope()