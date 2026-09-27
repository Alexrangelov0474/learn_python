list_of_cards = input().split(', ')
number_of_actions = int(input())

for current_action in range(number_of_actions):
    commands = input().split(', ')
    action = commands[0]
    if action == 'Add':
        card_name = commands[1]
        if card_name not in list_of_cards:
            list_of_cards.append(card_name)
            print('Card successfully added')
        else:
            print('Card is already in the deck')

    elif action == 'Remove':
        card_name = commands[1]
        if card_name in list_of_cards:
            list_of_cards.remove(card_name)
            print('Card successfully removed')
        else:
            print('Card not found')

    elif action == 'Remove At':
        index = int(commands[1])
        if 0 <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == 'Insert':
        index = int(commands[1])
        card_name = commands[2]
        if 0 <= index < len(list_of_cards):
            if card_name in list_of_cards:
                print('Card is already added')
            else:
                list_of_cards.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(', '.join(list_of_cards))
