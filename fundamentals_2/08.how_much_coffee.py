action = input()
coffees = 0

while action != 'END':
    if action.lower() in ('coding', 'dog', 'cat', 'movie'):

        if action.isupper():
            coffees += 2
        else:
            coffees += 1

    action = input()

if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)


