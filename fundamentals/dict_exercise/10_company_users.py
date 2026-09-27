companies = {}
while True:
    line = input().split(' -> ')
    if line[0] == 'End':
        break
    company = line[0]
    employee_id = line[1]
    if company not in companies.keys():
        companies[company] = []

    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employee_ids in companies.items():
    print(f'{company}')
    for employee in employee_ids:
        print(f'-- {employee}')
