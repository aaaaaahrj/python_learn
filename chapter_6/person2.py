khaye = {'name': 'khaye', 'last_name' : 'dacles', 'age' : '20', 'city' : 'mati'}
arj = {'name': 'arj', 'last_name' : 'tabudlong', 'age' : '20', 'city' : 'davao'}
james = {'name': 'james', 'last_name' : 'tabudlong', 'age' : '13', 'city' : 'mati'}

persons = [khaye, arj, james]

for person in persons:
    print(f"{person['name'].title()}'s Information:")
    for key, value in person.items():
        print(f"  {key.title()}: {value.title()}")
    print()

