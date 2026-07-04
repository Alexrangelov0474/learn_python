courses = {}

while True:

    booking = input().split()
    if booking[0] == 'finish':
        break

    course = booking[0].capitalize()
    student_name = booking[1]

    if course not in courses:
        courses[course] = []

    exists = False
    for current_student in courses[course]:
        if current_student.lower() == student_name.lower():
            exists = True
            break

    if not exists:
        courses[course].append(student_name)


total_courses = len(courses)
total_students = sum(len(names) for names in courses.values())

print('Courses: ')
for course, student_name in courses.items():
    students_char = ', '.join(student_name)
    print(f'{course}: {students_char}')
print(f'Total courses: {total_courses}')
print(f'Total students enrolled : {total_students}')



