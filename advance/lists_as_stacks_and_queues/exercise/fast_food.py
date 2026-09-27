from collections import deque

quantity_of_food = int(input())

queue = deque(int(x) for x in input().split())

print(max(queue))


while queue and queue[0] <= quantity_of_food:
    quantity_of_food -= queue.popleft()

if queue:
    print('Orders left:', *queue)
else:
    print('Orders complete')