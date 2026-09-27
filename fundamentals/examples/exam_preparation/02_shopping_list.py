groceries_list = input().split('!')
command = input()
while command != 'Go Shopping!':
    taken_command = command.split()
    action = taken_command[0]
    if action == 'Urgent':
        item = taken_command[1]
        if item not in groceries_list:
            groceries_list = [item] + groceries_list
    elif action == "Unnecessary":
        item = taken_command[1]
        if item in groceries_list:
            groceries_list.remove(item)
    elif action == "Correct":
        old_item = taken_command[1]
        new_item = taken_command[2]
        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item
    elif action == "Rearrange":
        item = taken_command[1]
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)
    command = input()
print(', '.join(groceries_list))
