people = [
    {"name":"Saad", "city":"Karachi"},
    {"name":"Babar", "city":"Lahore"},
    {"name":"Smith", "city":"Sydney"}
]

# var  = lambda parameter : returnThing

people.sort(key = lambda people : people["city"])

for person in people:
    print(person)
