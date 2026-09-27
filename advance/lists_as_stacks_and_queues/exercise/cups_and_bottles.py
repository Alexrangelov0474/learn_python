from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

water_wasted = 0

while cups and bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = bottles.pop()
        current_cup -= current_bottle

    water_wasted += abs(current_cup)
    cups.popleft()

if not cups:
    print('Bottles:', *bottles)

if not bottles:
    print('Cups:', *cups)

print(f'Wasted litters of water: {water_wasted}')