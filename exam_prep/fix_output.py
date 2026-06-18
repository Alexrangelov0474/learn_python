groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    taken_command = command.split()
    action = taken_command[0]
    item = taken_command[1]

    if action == "Urgent":
        if item not in groceries:
            groceries = [item] + groceries

    command = input()

print(", ".join(groceries))