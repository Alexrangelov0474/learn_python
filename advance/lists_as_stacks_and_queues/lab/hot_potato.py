from collections import deque

kids = deque(input().split())
number_of_rows = int(input())

while len(kids) > 1:
    kids.rotate(1 - number_of_rows)
    print(f'Removed {kids.popleft()}')

print(f'Last is {kids[0]}')