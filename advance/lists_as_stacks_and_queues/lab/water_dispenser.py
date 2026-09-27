from collections import deque

liters = int(input())
peoples = deque()

line = input()

while line != 'Start':
    peoples.append(line)
    line = input()

while line != 'End':
    if line.isdigit():
        person = peoples.popleft()
        liters_needed = int(line)
        if liters >= liters_needed:
            liters -= liters_needed
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif line.split()[0] == 'refill':
        liters += int(line.split()[1])

    line = input()

print(f'{liters} liters left')