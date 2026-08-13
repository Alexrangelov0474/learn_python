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
# result = dict(map(lambda student:(student[0], student[1] + 0.30), filtered_students))
#
# for name, grade in result.items():
#     print(f"{name}: {grade:.2f}")

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

# orders = [
#     {"customer": "Ivan", "total": 120, "status": "completed"},
#     {"customer": "Maria", "total": 80, "status": "pending"},
#     {"customer": "Petar", "total": 250, "status": "completed"},
#     {"customer": "Georgi", "total": 50, "status": "cancelled"},
#     {"customer": "Anna", "total": 180, "status": "completed"},
#     {"customer": "Stefan", "total": 90, "status": "completed"},
# ]
#
# filtered_orders = filter(lambda order: (order['status'] == 'completed' and order['total'] >= 100), orders)
# new_orders = list(map(lambda order: {'customer' : order['customer'], 'total' : order['total'] * 1.10}, filtered_orders))
# for current_order in new_orders:
#     print(f'{current_order["customer"]} : {current_order["total"]:.2f}')

# employees = [
#     {"name": "Ivan", "salary": 1800, "department": "IT"},
#     {"name": "Maria", "salary": 2200, "department": "HR"},
#     {"name": "Petar", "salary": 1500, "department": "IT"},
#     {"name": "Georgi", "salary": 2800, "department": "Finance"},
#     {"name": "Anna", "salary": 1900, "department": "HR"},
#     {"name": "Stefan", "salary": 1200, "department": "Finance"},
# ]
# filtered_employees = filter(lambda employee: (employee['department'] == 'IT' or employee['salary'] >= 2500),employees)
# new_employees = list(map(lambda employee: {'name' : employee['name'], 'salary' : employee['salary'] * 1.08}, filtered_employees))
# for current_employee in new_employees:
#     print(f'{current_employee["name"]}: {current_employee["salary"]:.2f}')

# products = [
#     {"name": "Laptop", "price": 1500, "rating": 4.7},
#     {"name": "Phone", "price": 900, "rating": 4.8},
#     {"name": "Monitor", "price": 400, "rating": 4.8},
#     {"name": "Keyboard", "price": 100, "rating": 4.5},
#     {"name": "Mouse", "price": 50, "rating": 4.7},
#     {"name": "Tablet", "price": 800, "rating": 4.9},
# ]
# filtered_products = filter(lambda product: product['price'] >= 500,  products)
# new_products = list(map(lambda product: {'name' : product['name'],
#                                          'price' : product['price'] * 1.10,
#                                          'rating' : product['rating']}, filtered_products))
#
# sorted_products = sorted(new_products, key=lambda product_dict: (-product_dict['rating'], -product_dict['price'], product_dict['name']))
# for product_as_dict in sorted_products:
#     print(f'{product_as_dict["name"]}: {product_as_dict["price"]:.2f} - {product_as_dict["rating"]:.2f}')
#
# players = [
#     {"name": "Ivan", "kills": 25, "deaths": 5, "rank": "gold"},
#     {"name": "Maria", "kills": 18, "deaths": 6, "rank": "silver"},
#     {"name": "Petar", "kills": 30, "deaths": 5, "rank": "gold"},
#     {"name": "Georgi", "kills": 20, "deaths": 10, "rank": "bronze"},
#     {"name": "Anna", "kills": 27, "deaths": 9, "rank": "gold"},
#     {"name": "Stefan", "kills": 22, "deaths": 4, "rank": "silver"},
# ]
#
# def get_kd(current_player: dict)-> float:
#     kills, deaths = current_player['kills'], current_player['deaths']
#     kd_ratio = kills / deaths
#     return kd_ratio
#
# filtered_players = filter(lambda player: (player['rank'] == 'gold' or player['kills'] >= 22), players)
# # new_players = list(map(lambda player: {'name' : player['name'], 'kd' : player['kills'] / player['deaths']}, filtered_players))
# new_players = list(map(lambda player: {'name' : player['name'], 'kd' : get_kd(player)}, filtered_players))
# sorted_players = sorted(new_players, key=lambda player_dict:(-player_dict['kd'], player_dict['name']))
#
# for player_as_dict in sorted_players:
#     print(f'{player_as_dict["name"]}: {player_as_dict["kd"]:.2f}')

# employees = [
#     {"name": "Ivan", "salary": 1800, "experience": 3, "department": "IT"},
#     {"name": "Maria", "salary": 2400, "experience": 5, "department": "HR"},
#     {"name": "Petar", "salary": 2200, "experience": 6, "department": "IT"},
#     {"name": "Georgi", "salary": 3000, "experience": 4, "department": "Finance"},
#     {"name": "Anna", "salary": 2000, "experience": 7, "department": "IT"},
#     {"name": "Stefan", "salary": 2600, "experience": 8, "department": "HR"},
# ]
#
# filtered_employees = filter(lambda employee: (employee['department'] == 'IT' or employee['salary'] >= 2500), employees)
# new_employees = list(map(lambda employee: {'name' : employee['name'],
#                                            'salary' : employee['salary'] * 1.10,
#                                            'experience' :  employee['experience']}, filtered_employees))
# sorted_employees = sorted(new_employees, key=lambda employee_dict: (-employee_dict['salary'], -employee_dict['experience'], employee_dict['name']))
# for employee_as_dict in sorted_employees:
#     print(f'{employee_as_dict["name"]}: {employee_as_dict["salary"]:.2f} - {employee_as_dict["experience"]} years')