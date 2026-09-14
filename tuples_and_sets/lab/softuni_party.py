number_of_guests = int(input())

reservations = set()

for _ in range(number_of_guests):
    reservations.add(input())


reservation = input()
while reservation != 'END':
    if reservation in reservations:
        reservations.remove(reservation)
        reservation = input()

print(len(reservations))
sorted_reservations = sorted(reservations)

for guest in sorted_reservations:
    print(guest)