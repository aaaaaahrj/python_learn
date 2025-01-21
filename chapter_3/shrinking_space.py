guests = ['Elon Musk', 'Donald Trump', 'Joe Biden']
missing = guests.pop()
print(f"{missing} can't attend.\n")

guests.append('Kamala Harris')

print(f"{guests[0]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[1]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[2]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")

print("\nI found a bigger table!\n")

guests.insert(0, "Mark Zuckerberg")
guests.insert(2, "Jeff Bezos")
guests.append("Geoff Keighley")

print(f"{guests[0]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[1]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[2]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[3]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[4]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[5]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")

print("\nNevermind, there is only space for two.\n")

print(f"{guests.pop()}, sorry you're not invited.")
print(f"{guests.pop()}, sorry you're not invited.")
print(f"{guests.pop()}, sorry you're not invited.")
print(f"{guests.pop()}, sorry you're not invited.\n")

print(f"{guests[0]}, you are invited to the inaugural dinner of the 47th President of the United States of America.")
print(f"{guests[1]}, you are invited to the inaugural dinner of the 47th President of the United States of America.\n")

del guests[1]
del guests[0]

print(guests)