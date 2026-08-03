# cities = {
#     "Varna": {
#         "Gold": 100,
#         "Wood": 50
#     },
#     "Sofia": {
#         "Gold": 80,
#         "Stone": 100
#     },
#     "Burgas": {
#         "Food": 150
#     }
# }
#
# sorted_cities = sorted(cities.items(), key=lambda city:(-len(city[1].values()), city[0]))
# print(sorted_cities)

# words = [
#     "banana",
#     "kiwi",
#     "apple",
#     "pear",
#     "watermelon"
# ]
#
# sorted(words, key=lambda fruits: (-len(fruits), fruits))

students = [
    ("Ivan", [6, 5, 6]),
    ("Maria", [6, 6, 6]),
    ("Petar", [5, 5, 5]),
    ("Georgi", [6, 5, 5])
]

sorted(students, key=lambda person: (-(sum(person[1]) / len(students[1])), students[0]))


