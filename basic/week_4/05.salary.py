n_open_tabs = int(input())
salary = int(input())

for _ in range(n_open_tabs):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(f'{salary}')