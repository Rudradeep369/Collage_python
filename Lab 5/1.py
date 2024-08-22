ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted Ages:", ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

# II. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

# III. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median Age:", median_age)

# IV. Find the average age
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

# V. Find the range of the ages
age_range = max_age - min_age
print("Age Range:", age_range)

# VI. Compare (min - average) and (max - average) using abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min-Average Difference:", min_diff)
print("Max-Average Difference:", max_diff)
