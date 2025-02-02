favorite_number = {'khaye' : [4, 2], 'arj' : [23, 69], 'james' : [5, 2], 'ian' : [7, 9], 'merna' : [5, 19]}


for n, v in favorite_number.items():
    print(f"{n.title()} favorite numbers are:")
    for number in v:
        print(f"  {number}")