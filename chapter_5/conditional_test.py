motor = 'mio'
car = 'mirage'
racket = 'yonex'
shuttle = 'used'
food = 'cookie'

#True statements
print(f"Is {motor} equal to Mio? I predict true.")
print(motor.title() == 'Mio')
print(f"Is {car} equal to Mirage? I predict true.")
print(car.title() == 'Mirage')
print(f"Is {racket} equal to Yonex? I predict true.")
print(racket.title() == 'Yonex')
print(f"Is {shuttle} equal to used? I predict true.")
print(shuttle == 'used')
print(f"Is {food} equal to cookie? I predict true.")
print(food == 'cookie')

#False statements
print(f"Is {motor} equal to Raider? I predict false.")
print(food == 'Raider')
print(f"Is {car} equal to Tesla? I predict true.")
print(car.title() == 'Tesla')
print(f"Is {racket} equal to Lining? I predict true.")
print(racket.title() == 'Lining')
shuttle = 'used'
print(f"Is {shuttle} equal to new? I predict true.")
print(shuttle == 'new')
food = 'cookie'
print(f"Is {food} equal to cake? I predict true.")
print(food == 'cake')


