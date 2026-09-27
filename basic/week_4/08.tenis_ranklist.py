n_tournaments = int(input())
starting_points = int(input())
total_points = 0
final_points = 0
p1 = 0

for _ in range(n_tournaments):
    position = input()
    if position == 'W':
        total_points += 2000
        p1 += 1
    elif position == 'F':
        total_points += 1200
    elif position == 'SF':
        total_points += 720

final_points = starting_points + total_points
average_points = total_points // n_tournaments
p1 = (p1 / n_tournaments) * 100

print(f"Final points: {final_points}\nAverage points: {average_points}\n{p1:.2f}%")