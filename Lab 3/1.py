# Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

s1=input('Enter Month : ')

def checkseason():
    if s1 == "December" or s1 =="January" or s1 =="February":
        print("Winter")
    elif s1 == "March" or  s1 =="April" or s1 =="May":
        print("Spring")
    elif s1 == "June" or  s1 =="July" or s1 =="August":
        print("Summer")
    else:
        print("Autumn")
    
checkseason()

# Output

# Enter Month : June
# Summer