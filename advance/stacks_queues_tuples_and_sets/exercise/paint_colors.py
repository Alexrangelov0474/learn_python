from collections import deque

substring = deque(input().split())

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}
colors_collected = []

while substring:
    first_string = substring.popleft()
    last_string = substring.pop() if substring else ''

    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            colors_collected.append(color)
            break
    else:
        if len(first_string) > 1:
            substring.insert(len(substring) // 2 , first_string[:-1])

        if len(last_string) > 1:
            substring.insert(len(substring) // 2 , last_string[:-1])

valid_colors = []
for color in colors_collected:
    if color in main_colors:
        valid_colors.append(color)
    elif color in secondary_colors:
        if all(primary_color in colors_collected for primary_color in secondary_colors[color]):
            valid_colors.append(color)

print(valid_colors)