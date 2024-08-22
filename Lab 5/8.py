# Create a dictionary mapping month numbers to seasons
month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall',
    11: 'Fall', 12: 'Winter'
}

# Get the month number (e.g., 4 for April)
month_number = 4

# Print the season based on the month number
season = month_to_season.get(month_number, 'Invalid month number')
print("Season:", season)
