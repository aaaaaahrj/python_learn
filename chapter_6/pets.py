cat = {'name' : 'enzo', 'owner' : 'shaye dacles', 'kind' : 'cat'}
dog = {'name' : 'ching ching', 'owner' : 'arj tabudlong', 'kind' : 'dog'}
bird = {'name' : 'rio', 'owner' : 'khaye dacles', 'kind' : 'bird'}
snake = {'name' : 'slink', 'owner' : 'billy panugan', 'kind' : 'snake'}
chicken = {'name' : 'bulaw', 'owner' : 'harvy panugan', 'kind' : 'chicken'}

pets = [cat, dog, bird, snake, chicken]

for pet in pets:
    print(f"Pet Information:")
    for n, v in pet.items():
        print(f"  {n.title()}: {v.title()}")
    print("")