cities = {
    'mati' : {'country' : 'philippines', 'population' : '20,000', 'fun fact' : 'Coconut capital of the Philippines'},
    'davao' : {'country' : 'philippines', 'population' : '60,000', 'fun fact' : 'Durian capital of the Davao Region'},
    'manila' : {'country' : 'philippines', 'population' : '100,000', 'fun fact' : 'Capital of the Philippines'}
    }

for name, value in cities.items():
    print(f"{name.title()} City:")
    for x, y in value.items():
        print(f"  {x.title()}: {y.title()}")