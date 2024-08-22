fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'egg', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print("Joined Tuple:", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("List from Tuple:", food_stuff_lt)

n = len(food_stuff_lt)
middle_items = food_stuff_lt[n//2] if n % 2 != 0 else food_stuff_lt[n//2 - 1:n//2 + 1]
print("Middle Item(s):", middle_items)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First Three Items:", first_three)
print("Last Three Items:", last_three)

del food_stuff_tp
