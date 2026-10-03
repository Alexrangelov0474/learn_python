PUNK = {"-", ",", ".", "!", "?"}

with open('text.txt') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            for char in PUNK:
                line = line.replace(char, '@')

            print(*reversed(line.split()))
            