text = input()
for index in range(len(text) -1):
    if text[index] == ':':
        print(f':{text[index + 1]}')
