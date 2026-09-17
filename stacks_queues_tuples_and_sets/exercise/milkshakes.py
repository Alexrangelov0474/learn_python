from collections import deque
from typing import Iterable

def printer(name:str, items: Iterable[int]) -> None:
    if items:
        print(f'{name}: {", ".join(map(str, items))}')
    else:
        print(f'{name}: empty')

chocolate = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int,input().split(', ')))
milkshakes = 0

while chocolate and cups_of_milk and milkshakes < 5:

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolate[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolate.pop()
        cups_of_milk.popleft()
    else:
        current_ingredient = cups_of_milk.popleft()
        cups_of_milk.append(current_ingredient)
        chocolate[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

printer('Chocolate', chocolate)
printer('Milk', cups_of_milk)