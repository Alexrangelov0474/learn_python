number_of_lines = int(input())

students_data = {}

for line in range(number_of_lines):
    name, grade = input().split()
    if name not in students_data:
        students_data[name] = []
    students_data[name].append(float(grade))

for name, grades in students_data.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {average_grade:.2f})")