classroom = {}
while True:
    status = input().split()
    if status[0] == 'finish':
        break
    student = status[0]
    action = status[1]

    classroom[student] = action

present = 0
absent = 0
print('Attendance:')
for students, actions in classroom.items():
    if actions == 'present':
        present += 1
    elif actions == 'absent':
        absent += 1

    print(f'{students}: {actions}')

print(f'present: {present}')
print(f'absent: {absent}')


