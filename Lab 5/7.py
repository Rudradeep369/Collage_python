# Create the person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if the person dictionary has skills key, if so print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# II. Check if the person has 'Python' skill and print the result
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# III. Determine the person's role based on their skills
if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('He is a front-end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(person['skills']):
    print('He is a back-end developer')
elif {'React', 'Node', 'MongoDB'}.issubset(person['skills']):
    print('He is a fullstack developer')
else:
    print('unknown title')

# IV. Print information if the person is married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
