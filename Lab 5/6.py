student = {
    'first_name': 'Rudradeep',
    'last_name': 'Debnath',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Django,Bootstrap,tailwind,js'],
    'country': 'INDIA',
    'city': 'Kolkata',
    'address': 'Kolkata 123'
}
# I. Get the length of the student dictionary
length = len(student)
print("Length of student dictionary:", length)
# II. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))
# III. Modify the skills values by adding one or two skills
student['skills'].extend(['JavaScript', 'React'])
print("Updated Skills:", student['skills'])
# IV. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary Keys:", keys)
# V. Get the dictionary values as a list
values = list(student.values())
print("Dictionary Values:", values)
# VI. Change the dictionary to a list of tuples using items() method
items = list(student.items())
print("List of Tuples:", items)
# VII. Delete one of the items in the dictionary
student.pop('marital_status')
print("Dictionary after deleting marital_status:", student)
# VIII. Delete the student dictionary
del student
