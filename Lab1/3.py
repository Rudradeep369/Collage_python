# WAP to check whether a given year is leap year or not

y = int(input("Enter year: "))

if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
    print(f"{y} is a Leap year")
else:
    print(f"{y} is not a Leap year")