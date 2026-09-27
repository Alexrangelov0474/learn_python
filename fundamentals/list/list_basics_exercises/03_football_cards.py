team_a = [f'A-{i}' for i in range(1, 12)]
team_b = [f'B-{i}' for i in range(1, 12)]
game_stopped = False

players = input().split()
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_stopped = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_stopped:
    print('Game was terminated')