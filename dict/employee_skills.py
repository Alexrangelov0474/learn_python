employees = {}

while True:
    line = input().split()
    if line[0] == 'done':
        break

    name = line[0]
    skill = line[1]

    if name not in employees:
        employees[name] = []
        employees[name].append(skill)
    elif skill not in employees[name]:
        employees[name].append(skill)
    else:
        continue

total_employees = len(employees)

print('Employees')
for name, skill in employees.items():
    print(f'{name}: {", ".join(skill)}')
print(f'Total employees: {total_employees}')