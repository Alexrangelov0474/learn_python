courses = {}
while True:
    booking = input().split(' : ')
    if booking[0] == 'end':
        break

    course, name = booking[0], booking[1]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(name)

for course_name, students_names in courses.items():
    print(f'{course_name}: {len(students_names)}')
    for student in students_names:
        print(f'-- {student}')

