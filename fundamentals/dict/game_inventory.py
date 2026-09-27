inventory = {}
while True:
    player_and_game = input().split()
    if player_and_game[0] == 'stop':
        break
    player = player_and_game[0]
    game = player_and_game[1]

    player_exist = False
    for current_player in inventory.keys():
        if current_player.lower() == player.lower():
            player_exist = True
            player = current_player
            break

    if not player_exist:
        inventory[player] = []

    game_already_taken = False
    for current_player in inventory.keys():
        for current_game in inventory[current_player]:
            if current_game.lower() == game.lower():
                game_already_taken = True
                break

        if game_already_taken:           #<<<----- Прекъсваме и външния цикъл когато сме намерили,
            break                        # че играта съществува при някой играч, защото няма нужда
                                         # да проверяваме останалите хора


    if not game_already_taken:
        inventory[player].append(game)


total_users = len(inventory)
total_games = sum(len(some_game) for some_game in inventory.values())

print('Users:')
for users, games in inventory.items():
    print(f'{users} -> {", ".join(games)}')

print(f'Total users: {total_users}')
print(f'Total games: {total_games}')