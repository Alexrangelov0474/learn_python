number_of_rooms = int(input())
total_free_chairs = 0

for number_of_room in range(1,number_of_rooms + 1):
    number_of_chairs, number_of_peoples = input().split()
    difference = len(number_of_chairs) - int(number_of_peoples)
    if difference < 0:
        print(f'{abs(difference)} more chairs needed in room {number_of_room}')

    total_free_chairs += difference
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')