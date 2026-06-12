wagons = [0] * int(input())

while True:
    action = input().split()
    current_action = action[0]
    if current_action == 'End':
        print(wagons)
        break
    elif current_action == 'add':
        people_amount = int(action[1])
        wagons[-1] += people_amount

    elif current_action == 'insert':
        index = int(action[1])
        peoples = int(action[2])
        wagons[index] += peoples
    elif current_action == 'leave':
        index = int(action[1])
        peoples = int(action[2])
        wagons[index] -= peoples


