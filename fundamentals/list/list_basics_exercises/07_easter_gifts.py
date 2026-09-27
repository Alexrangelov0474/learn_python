gifts_planned_to_buy = input().split()
while True:
    command = input()
    if command == "No Money":
        break
    gift = command.split()
    action = gift[0]

    if action == "OutOfStock":
        the_gift = gift[1]
        for index in range(len(gifts_planned_to_buy)):
            if gifts_planned_to_buy[index] == the_gift:
                gifts_planned_to_buy[index] = "None"

    elif action == "Required":
        the_gift = gift[1]
        index = int(gift[2])
        if 0 <= index < len(gifts_planned_to_buy):
            gifts_planned_to_buy[index] = the_gift

    elif action == "JustInCase":
        the_gift = gift[1]
        gifts_planned_to_buy[-1] = the_gift

result = []

for gift in gifts_planned_to_buy:
    if gift != "None":
        result.append(gift)

print(" ".join(result))