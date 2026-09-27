force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(' | ')
        force_user_already_exist = False
        for list_with_force_users in force_side_dictionary.values():
            if force_user in list_with_force_users:
                force_user_already_exist = True
                break
        if not force_user_already_exist:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(' -> ')
        for list_with_force_users in force_side_dictionary.values():
            if force_user in list_with_force_users:
                list_with_force_users.remove(force_user)
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()
for force_side, list_with_force_users in force_side_dictionary.items():
    if list_with_force_users:
        print(f'Side: {force_side}, Members: {len(list_with_force_users)}')
        for force_user in list_with_force_users:
            print(f'! {force_user}')