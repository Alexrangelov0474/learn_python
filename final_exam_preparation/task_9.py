import re
def extract_data(text:str) -> dict:
    pattern = r'([%@])([A-Z][A-Za-z]{2,})\1<([A-Z][a-z]{2,})>'
    some_employees = {}

    for match in re.finditer(pattern, text):
        employee_name = match.group(2)
        employee_skill = match.group(3)
        if employee_name not in some_employees.keys():
            some_employees[employee_name] = []

        some_employees[employee_name].append(employee_skill)
    return some_employees

def add_skill(employees_dict: dict,some_name:str, some_skill: str) -> None:
    if some_name in employees_dict.keys() and some_skill not in employees_dict[some_name]:
        employees_dict[some_name].append(some_skill)

def remove_skill(employees_dict: dict, some_name:str, some_skill: str) -> None:
    if some_name in employees_dict.keys():
        if some_skill in employees_dict[some_name]:
            employees_dict[some_name].remove(some_skill)


def replace_skill(employees_dict: dict,some_name:str, some_skill: str) -> None:
    if some_name in employees_dict.keys():
        current_skills = employees_dict[some_name]
        if current_skills:
            employees_dict[some_name][0] = some_skill




string = input()
employees = extract_data(string)

while True:
    command = input()
    if command == 'End':
        break
    action, name, skill = command.split(':')
    if action == 'Add':
        add_skill(employees,name,skill)
    elif action == 'Remove':
        remove_skill(employees,name,skill)
    elif action == 'Replace':
        replace_skill(employees, name,skill)

for name, skills in employees.items():
    print(f'{name}:')
    for skill in skills:
        print(f'- {skill}')
