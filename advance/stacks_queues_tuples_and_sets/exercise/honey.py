from collections import deque

bees = deque(map(int,input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

operators = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y if y != 0 else 0
}


total_honey = 0

while bees and nectar:
    current_nectar = nectar.pop()
    if current_nectar >= bees[0]:
        current_bee = bees.popleft()
        current_symbol = symbols.popleft()
        total_honey += abs(operators[current_symbol](current_bee, current_nectar))


print(f'Total honey made: {total_honey}')

if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
elif nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
