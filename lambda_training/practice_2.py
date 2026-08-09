# books = [
#     ("Python Basics", 350, 4.8),
#     ("Algorithms", 500, 4.9),
#     ("Data Structures", 500, 4.7),
#     ("HTML & CSS", 250, 4.9),
# ]
#
# sorted_books = sorted(books, key=lambda book: (-book[1], -book[2], book[0]))
# print(sorted_books)


# cities = {
#     "Varna": {
#         "Gold": 100,
#         "Wood": 80,
#         "Stone": 40
#     },
#     "Sofia": {
#         "Gold": 50,
#         "Wood": 50
#     },
#     "Burgas": {
#         "Food": 300
#     }
# }
# cities_with_average = []
# for city, resources in cities.items():
#     average_amount = sum(resources.values()) / len(resources)
#     cities_with_average.append((city,average_amount))
#
# sorted_cities = sorted(cities_with_average, key=lambda current_city: (-current_city[1], current_city[0]))
#
# for city, average_resource in sorted_cities:
#     print(f"{city} -> {average_resource:.2f}")


# players = [
#     ("Ivan", {"kills": 15, "deaths": 3}),
#     ("Maria", {"kills": 20, "deaths": 10}),
#     ("Petar", {"kills": 12, "deaths": 2}),
#     ("Georgi", {"kills": 20, "deaths": 5}),
# ]
#
# players_average = []
#
# for player_name, kills_and_deaths in players:
#     kills = kills_and_deaths["kills"]
#     deaths = kills_and_deaths["deaths"]
#     kd_ratio = kills / deaths
#     players_average.append((player_name, kd_ratio))
#
# sorted_players = sorted(players_average, key=lambda current_player: (-current_player[1], current_player[0]))
#
# for player, kd in sorted_players:
#     print(f"{player} -> {kd}")



# players = [
#     ("Ivan", {"kills": 15, "deaths": 3}),
#     ("Maria", {"kills": 20, "deaths": 10}),
#     ("Petar", {"kills": 12, "deaths": 2}),
#     ("Georgi", {"kills": 20, "deaths": 5}),
# ]
#
# kd_players = []
#
# for player_name, kd_stats in players:
#     kills = kd_stats['kills']
#     deaths = kd_stats['deaths']
#     kd_ration = kills/deaths
#     kd_players.append((player_name, kd_ration, kills))
#
# sorted_players = sorted(kd_players, key=lambda current_player: (-current_player[1], -current_player[2], current_player[0]))
#
# for name, kd, kills in sorted_players:
#     print(f"{name} -> {kd}")



# students = [
#     ("Ivan", [6, 5, 6]),
#     ("Maria", [4, 5, 4]),
#     ("Petar", [6, 6, 6]),
#     ("Georgi", [5, 5, 5]),
# ]
#
# sorted_students = sorted(students, key=lambda student: (sum(student[1]) / len(student[1]) < 5, -(sum(student[1]) / len(student[1])), student[0]))
#
# print(sorted_students)



# products = [
#     ("Laptop", 1500, 4.7),
#     ("Phone", 900, 4.8),
#     ("Monitor", 400, 4.8),
#     ("Keyboard", 100, 4.5),
#     ("Mouse", 50, 4.7)
# ]
#
# sorted_products = sorted(products, key=lambda product: (-product[2], product[1], product[0]))
# print(sorted_products)
#
# cities = {
#     "Varna": {"Gold": 100, "Wood": 50},
#     "Sofia": {"Gold": 80, "Stone": 100},
#     "Burgas": {"Food": 150},
#     "Plovdiv": {"Gold": 70, "Wood": 80}
# }
#
# sorted_cities = sorted(cities.items(), key=lambda current_city: (-(sum(current_city[1].values())), current_city[0]))
# print(sorted_cities)

# employees = [
#     ("Ivan", 3200, 5),
#     ("Maria", 4500, 2),
#     ("Petar", 4500, 7),
#     ("Georgi", 3200, 10),
#     ("Anna", 3200, 10)
# ]
#
# sorted_employees = sorted(employees, key=lambda current_employeer: (-current_employeer[1], - current_employeer[2], current_employeer[0]))
# print(sorted_employees)


# players = {
#     "Ivan": {"kills": 25, "deaths": 5},
#     "Maria": {"kills": 30, "deaths": 10},
#     "Petar": {"kills": 20, "deaths": 2},
#     "Georgi": {"kills": 30, "deaths": 5},
# }
#
# players_kd_ratio = []
#
# def c(current_player_kd: dict)-> float:
#     kills = current_player_kd['kills']
#     deaths = current_player_kd['deaths']
#     current_kd_ratio = kills / deaths
#     return current_kd_ratio
#
# for player_name, player_data in players.items():
#     kd_ratio = get_kd_ratio(player_data)
#     players_kd_ratio.append((player_name, kd_ratio, player_data['kills']))
#
#
# sorted_players = sorted(players_kd_ratio, key=lambda current_player: \
#     (-current_player[1], -current_player[2], current_player[0]))
# print(sorted_players)


# players = [
#     ("Ivan", 25, 5),
#     ("Maria", 30, 10),
#     ("Petar", 20, 2),
#     ("Georgi", 30, 5),
#     ("Anna", 25, 5)
# ]
#
# players_kd_ratio = []
#
# def get_kd_ratio(current_kills:int, current_deaths:int) -> float:
#     current_kd_ratio = current_kills / current_deaths
#     return current_kd_ratio
#
# for players_data in players:
#     player_name = players_data[0]
#     kills = players_data[1]
#     deaths = players_data[2]
#     kd_ratio = get_kd_ratio(kills,deaths)
#     players_kd_ratio.append((player_name, kd_ratio, kills))
#
# sorted_players = sorted(players_kd_ratio, key=lambda player: (-player[1], -player[2], player[0]))
# print(sorted_players)

#
# products = [
#     ("Laptop", 1500, 4.7, 120),
#     ("Phone", 900, 4.8, 250),
#     ("Monitor", 400, 4.8, 180),
#     ("Keyboard", 100, 4.5, 300),
#     ("Mouse", 50, 4.7, 150)
# ]
#
# sorted_products = sorted(products, key=lambda product: (-product[2], -product[3], product[1]))
# print(sorted_products)

# players = [
#     ("Ivan", {"kills": 25, "deaths": 5}),
#     ("Maria", {"kills": 30, "deaths": 10}),
#     ("Petar", {"kills": 20, "deaths": 2}),
#     ("Georgi", {"kills": 30, "deaths": 5}),
#     ("Anna", {"kills": 25, "deaths": 5}),
# ]
#
# players_with_kd = []
#
# def get_kd_ratio(current_kills:int, current_deaths:int) -> float:
#     current_kd_ratio = current_kills / current_deaths
#     return current_kd_ratio
#
# for player_data in players:
#     player_name = player_data[0]
#     kills = player_data[1]['kills']
#     deaths = player_data[1]['deaths']
#     kd_ratio = get_kd_ratio(kills, deaths)
#     players_with_kd.append((player_name, kd_ratio, kills))
#
# sorted_players = sorted(players_with_kd, key=lambda player: (-player[1], -player[2], player[0]))
# print(sorted_players)


# products = [
#     ("Laptop", 1500, 4.7, 120),
#     ("Phone", 900, 4.8, 250),
#     ("Monitor", 400, 4.8, 180),
#     ("Keyboard", 100, 4.5, 300),
#     ("Mouse", 50, 4.7, 150),
# ]
#
# sorted_products = sorted(products, key=lambda product: (-product[2], -product[3], product[1], product[0]))
# print(sorted_products)

# cities = {
#     "Sofia": {"population": 1200000, "area": 492, "rating": 4.5},
#     "Varna": {"population": 350000, "area": 238, "rating": 4.7},
#     "Burgas": {"population": 200000, "area": 253, "rating": 4.7},
#     "Plovdiv": {"population": 340000, "area": 102, "rating": 4.5},
#     "Ruse": {"population": 150000, "area": 127, "rating": 4.2},
# }
#
# sorted_cities = sorted(cities.items(), key=lambda city: (-city[1]['rating'],
#                                                          -city[1]['population'],
#                                                          -city[1]['area'],
#                                                          city[0]))
# print(sorted_cities)

# employees = [
#     ("Ivan", {"salary": 3200, "experience": 5, "projects": 12}),
#     ("Maria", {"salary": 4500, "experience": 2, "projects": 20}),
#     ("Petar", {"salary": 4500, "experience": 7, "projects": 15}),
#     ("Georgi", {"salary": 3200, "experience": 10, "projects": 12}),
#     ("Anna", {"salary": 3200, "experience": 10, "projects": 18}),
# ]
#
# sorted_employees = sorted(employees, key=lambda employee: (-employee[1]['salary'],
#                                                            -employee[1]['experience'],
#                                                            -employee[1]['projects'],
#                                                            employee[0]))
# print(sorted_employees)


# games = [
#     ("CS2", 120, 8.5, 150),
#     ("Minecraft", 200, 9.0, 100),
#     ("GTA V", 150, 8.5, 200),
#     ("Valorant", 100, 8.8, 180),
#     ("R6 Siege", 80, 8.5, 200),
# ]
#
# sorted_games = sorted(games, key=lambda game: (-game[2],-game[3], game[1], game[0]))
# print(sorted_games)

# students = [
#     ("Ivan", [6, 5, 6]),
#     ("Maria", [4, 5, 4]),
#     ("Petar", [6, 6, 5]),
#     ("Georgi", [5, 5, 5]),
#     ("Anna", [4, 4, 5]),
# ]
# sorted_students = sorted(students, key=lambda student: (-(sum(student[1]) / len(student[1]) >= 5),
#                                                         -(sum(student[1]) / len(student[1])), student[0]))
# print(sorted_students)

# employees = [
#     ("Ivan", {"salary": 3200, "experience": 5, "projects": 12}),
#     ("Maria", {"salary": 4500, "experience": 2, "projects": 20}),
#     ("Petar", {"salary": 4500, "experience": 7, "projects": 15}),
#     ("Georgi", {"salary": 3200, "experience": 10, "projects": 12}),
#     ("Anna", {"salary": 3200, "experience": 10, "projects": 18}),
#     ("Stefan", {"salary": 4500, "experience": 7, "projects": 15}),
# ]
#
# sorted_employees = sorted(employees, key=lambda employee: (-employee[1]['salary'],
#                                                            -employee[1]["experience"],
#                                                            -employee[1]["projects"],
#                                                            employee[0]))
# print(sorted_employees)

# products = [
#     ("Laptop", {"price": 1500, "rating": 4.7, "sales": 120}),
#     ("Phone", {"price": 900, "rating": 4.8, "sales": 250}),
#     ("Monitor", {"price": 400, "rating": 4.8, "sales": 180}),
#     ("Keyboard", {"price": 100, "rating": 4.5, "sales": 300}),
#     ("Mouse", {"price": 50, "rating": 4.7, "sales": 150}),
#     ("Tablet", {"price": 900, "rating": 4.8, "sales": 250}),
# ]
#
# sorted_employees = sorted(products, key=lambda product:(-product[1]['rating'],
#                                                         -product[1]['sales'],
#                                                         product[1]['price'],
#                                                         product[0]))
#
# print(sorted_employees)

