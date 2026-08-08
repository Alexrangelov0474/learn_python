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


