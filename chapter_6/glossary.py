glossary = {
    'loop' : 'A repeated sequence of code.', 
    'boolean' : 'Has only 2 values, either true or false.', 
    'dictionary' : 'Stores data in key-value pairs.', 
    'list' : 'Stores an ordered sequence of data with the same type.',
    'tuple' : 'Store an immutable sequence of data with the same type.'
    }

print("Glossary:")
for key, value in glossary.items():
    print(f"{key.title()}: {value}")