
#
# people = [
#     ("Ivan", 25),
#     ("Maria", 19),
#     ("Petar", 25),
#     ("Georgi", 22)
# ]
# # by age
# sorted(people, key=lambda person: person[1])
#
# #by age but if same, by name
# sorted(people, key=lambda person: (person[0], person[1]))

students = [
    ("Ivan", 5.50),
    ("Maria", 6.00),
    ("Petar", 4.80),
    ("Georgi", 6.00)
]
#by grade
sorted(students, key=lambda person: person[1])

sorted(students, key=lambda person: (-person[1], person[0]))

