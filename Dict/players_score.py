players = {}

while True:
    line = input().split()
    if line[0] == 'stop':
        break

    name = line[0]
    score = int(line[1])

    if name not in players:
        players[name] = score
    else:
        players[name] += score

total_players = len(players)
total_score = sum(players.values())
print('Players:')
for name, score in players.items():
    print(f'{name}: {score}')

print(f'Total Players: {total_players}\n'
      f'Total Score: {total_score}')