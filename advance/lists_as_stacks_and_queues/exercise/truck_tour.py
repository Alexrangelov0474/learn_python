from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    current_fuel, current_distance = input().split()
    pumps.append({'fuel': int(current_fuel), 'dist': int(current_distance)})

start_position = 0
stops = 0

while stops < petrol_pumps:
    fuel = 0
    for idx in range(petrol_pumps):
        fuel += pumps[idx]['fuel']
        distance = pumps[idx]['dist']
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break

        fuel -= distance
        stops += 1

print(start_position)