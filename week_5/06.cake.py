width = int(input())
length = int(input())

pieces_cake = width * length

command = input()

while command != 'STOP':
    piece_taken = int(command)
    pieces_cake -= piece_taken
    if pieces_cake < 0:
        print(f"No more cake left! You need {abs(pieces_cake)} pieces more.")
        break

    command = input()
else:
    print(f"{pieces_cake} pieces are left.")