phonebook = {}
while True:
    entry = input()
    if '-' not in entry:
        break
    name, phone_number = entry.split('-')
    phonebook[name] = phone_number

number_of_searches = int(entry)
for current_search in range(number_of_searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        number = phonebook[searched_name]
        print(f'{searched_name} -> {number}')
    else:
        print(f'Contact {searched_name} does not exist.')