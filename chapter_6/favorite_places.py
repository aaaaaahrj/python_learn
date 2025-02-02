favorite_places = {'khaye' : ['mati', 'davao', 'capitol'], 'arj' : ['japan', 'switzerland', 'canada'], 'ian' : ['korea', 'america', 'thailand']}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"   {place.title()}")
