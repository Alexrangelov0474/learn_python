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
#
# products = {
#     "Laptop": 1500,
#     "Phone": 900,
#     "Monitor": 400,
#     "Keyboard": 100,
#     "Mouse": 50,
#     "Tablet": 800
# }
#
#
# filtered_products = filter(lambda product: product[1] >= 500 , products.items())
# result = dict(map(lambda product: (product[0], round(product[1] * 1.20, 2)), filtered_products))
# print(result)

# employees = {
#     "Ivan": 1200,
#     "Maria": 1800,
#     "Petar": 950,
#     "Georgi": 2200,
#     "Anna": 1600,
#     "Stefan": 800
# }
#
# filtered_employees = filter(lambda employee: employee[1] >= 1200, employees.items())
# result = dict(map(lambda employee: (employee[0], round(employee[1] * 1.10, 2)), filtered_employees))
# print(result)

# students = {
#     "Ivan": 5.20,
#     "Maria": 4.30,
#     "Petar": 5.80,
#     "Georgi": 3.90,
#     "Anna": 5.50,
#     "Stefan": 4.90
# }
#
# filtered_students = filter(lambda student: student[1] >= 5.00, students.items())
# result = dict(map(lambda student:(student[0], student[1] + 0.30, 2), filtered_students))
#
# for name, grade in result.items():
#     print(f"{name} :{grade:.2f}")

# students = [
#     {"name": "Ivan", "grade": 5.20},
#     {"name": "Maria", "grade": 4.30},
#     {"name": "Petar", "grade": 5.80},
#     {"name": "Georgi", "grade": 3.90},
#     {"name": "Anna", "grade": 5.50},
#     {"name": "Stefan", "grade": 4.90}
# ]
#
# filtered_students = list(filter(lambda student: student['grade'] >= 5.00, students))
# result = list(map(lambda student: {'name' : student['name'], 'grade' : student['grade'] + 0.20},  filtered_students))
# for current_student in result:
#     print(f"{current_student['name']}: {current_student['grade']:.2f}")

# products = [
#     {"name": "Laptop", "price": 1500, "category": "Electronics"},
#     {"name": "Phone", "price": 900, "category": "Electronics"},
#     {"name": "Desk", "price": 350, "category": "Furniture"},
#     {"name": "Monitor", "price": 600, "category": "Electronics"},
#     {"name": "Chair", "price": 250, "category": "Furniture"},
#     {"name": "Keyboard", "price": 120, "category": "Electronics"},
# ]
# filtered_products = (filter(lambda product: (product['category'] == 'Electronics' and product['price'] >= 500), products))
# result = list(map(lambda product: {'name' : product['name'], 'price' : product['price'] * 1.15}, filtered_products))
# for current_product in result:
#     print(f'{current_product["name"]}: {current_product["price"]:.2f}')

