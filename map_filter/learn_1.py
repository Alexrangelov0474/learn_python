# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = list(map(lambda number: number ** 2, numbers))
# print(result)

# numbers = [3, 8, 11, 14, 17, 20, 23, 26]
# result = list(filter(lambda number: number % 2 == 0, numbers))
# final_result = list(map(lambda number: number * 2, result))
# print(final_result)

# players = [
#     ("Ivan", 25),
#     ("Maria", 18),
#     ("Petar", 30),
#     ("Georgi", 16),
#     ("Anna", 22)
# ]
#
# filtered_players = list(filter(lambda player: player[1] >= 21, players))
# print(filtered_players)

# players = [
#     ("Ivan", 25),
#     ("Maria", 18),
#     ("Petar", 30),
#     ("Georgi", 16),
#     ("Anna", 22),
# ]
# filtere_players = list(filter(lambda player: player[1] >= 21, players))
# result = list(map(lambda player: player[0], filtere_players))
# print(result)

# products = [
#     ("Laptop", 1500),
#     ("Phone", 900),
#     ("Monitor", 400),
#     ("Keyboard", 100),
#     ("Mouse", 50),
# ]
# filtered_products = list(filter(lambda product: product[1] >= 400, products))
# result = list(map(lambda product: product[0], filtered_products))
# print(result)


# students = [
#     ("Ivan", 5.50),
#     ("Maria", 4.20),
#     ("Petar", 5.80),
#     ("Georgi", 3.90),
#     ("Anna", 5.10),
# ]

# !!!!!!!! ВАРИАНТИ ЗА МАНИПУЛИРАНЕ НА ЛАМБДАТА. МОЖЕ ДА ВРЪЩА КАКВОТО МУ ЗАДАДЕМ.!!!!!!!!!

# filtered_students = list(filter(lambda student: student[1] >= 5.00, students))
# result = list(map(lambda student: (student[0],student[1] + 0.50), filtered_students))
# result = list(map(lambda student: {"name": student[0],"grade": student[1] + 0.5}, filtered_students))
# result = tuple(map(lambda student: {"name": student[0],"grade": student[1] + 0.5}, filtered_students))
# result = dict(map(lambda student: (student[0], student[1] + 0.5), filtered_students))
# result = list(map(lambda student:{'student': (student[0], student[1] + 0.5)}, filtered_students))
# print(result)

# players = [
#     ("Ivan", 25),
#     ("Maria", 18),
#     ("Petar", 30),
#     ("Georgi", 16),
#     ("Anna", 22),
#     ("Stefan", 19),
# ]
#
# filtered_players = list(filter(lambda player: player[1] >= 21, players))
# print(filtered_players)


# filter_players = list(filter(lambda player: player[1] >= 20, players))
# result = list(map(lambda player: player[0], filter_players))
# print(result)


# products = [
#     ("Laptop", 1500),
#     ("Phone", 900),
#     ("Monitor", 400),
#     ("Keyboard", 100),
#     ("Mouse", 50),
#     ("Tablet", 800),
# ]
# filtered_products = list(filter(lambda product: product[1] >= 500, products))
# result = list(map(lambda product: (product[0], round(product[1] * 1.10, 2)) , filtered_products))
#
# print(result)

# players = {
#     "Ivan": 25,
#     "Maria": 18,
#     "Petar": 30,
#     "Georgi": 16,
#     "Anna": 22,
#     "Stefan": 19,
# }
#
# filtered_products = (filter(lambda player: player[1] >= 20, players.items()))
# result = dict(map(lambda player: (player[0], player[1] + 1), filtered_products))
# print(result)