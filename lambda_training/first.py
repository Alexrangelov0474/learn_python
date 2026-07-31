people = [
    ("Ivan", 25),
    ("Maria", 19),
    ("Petar", 31)
]

def get_age(people_data):
    return people_data[1]

sorted_peoples = sorted(people, key=get_age)
print(sorted_peoples)