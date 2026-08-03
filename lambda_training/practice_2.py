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

players = [
    ("Ivan", {"kills": 15, "deaths": 3}),
    ("Maria", {"kills": 20, "deaths": 10}),
    ("Petar", {"kills": 12, "deaths": 2}),
    ("Georgi", {"kills": 20, "deaths": 5}),
]

players_average = []

for player_name, kills_and_deaths in players:
    kills = kills_and_deaths["kills"]
    deaths = kills_and_deaths["deaths"]
    kd_ratio = kills / deaths
    players_average.append((player_name, kd_ratio))

sorted_players = sorted(players_average, key=lambda current_player: (-current_player[1], current_player[0]))

for player, kd in sorted_players:
    print(f"{player} -> {kd}")