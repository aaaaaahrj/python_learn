rivers = {'nile' : 'river', 'pasig' : 'philippines', 'amazon' : 'brazil'}

print("Rivers:")
for river in rivers.keys():
    print(f"  -{river.title()}")

print("Countries")
for country in rivers.values():
    print(f"  -{country.title()}")

print("")
for river, country in rivers.items():
    print(f"The {river.title()} is located in {country.title()}")

