favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

people = ['khaye', 'jhoneah', 'phil', 'arianne']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for answering our poll, {person.title()}")
    else:
        print(f"Please answer our poll, {person.title()}")