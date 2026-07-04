teams = {}
while True:
    line = input().split()
    if line[0] == 'stop':
        break

    team = line[0]
    player = line[1]

    team_exists = False
    for current_team in teams:
        if current_team.lower() == team.lower():
            team_exists = True
            team = current_team
            break
    player_in_other_team = False

    for current_team in teams:
        for current_player in teams[current_team]:
            if current_player.lower() == player.lower():
                player_in_other_team = True
                break

        if player_in_other_team:
            break

    if player_in_other_team:
        continue

    if not team_exists:
        teams[team] = []

    player_exists = False
    for current_player in teams[team]:

        if current_player.lower() == player.lower():
            player_exists = True
            break
    if not player_exists:
        teams[team].append(player)


total_teams = len(teams)
total_players = sum(len(players) for players in teams.values())

print('Teams: ')
for team, players in teams.items():
    players_char = ', '.join(players)
    print(f'{team}: {players_char}')
print(f'Total teams: {total_teams}')
print(f'Total players : {total_players}')
