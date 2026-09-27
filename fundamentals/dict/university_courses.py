university = {}
while True:
    booking = input().split()
    if booking[0] == 'end':
        break

    course = booking[0]
    student = booking[1]

    course_exist = False
    for current_course in university.keys():
        if current_course.lower() == course.lower():
            course_exist = True
            course = current_course
            break

    if not course_exist:
        university[course] = []

    exist_counter = 0
    student_exist_two_times = False
    for current_course in university.keys():
        for current_student in university[current_course]:
            if current_student.lower() == student.lower():
                exist_counter += 1
                student = current_student
                break

        if exist_counter >= 2:
            student_exist_two_times = True
            break

    student_exist = False
    for current_student in university[course]:
        if current_student.lower() == student.lower():
            student_exist = True
            break

    if not student_exist_two_times and not student_exist:
        university[course].append(student)

empty_courses = []
for course,students in university.items():
    if len(students) == 0:
        empty_courses.append(course)

for course in empty_courses:
    del university[course]


total_courses = len(university)
total_students = sum(len(students) for students in university.values())

print('Courses: ')
for some_courses, some_students in university.items():
    print(f'{some_courses} -> {", ".join(some_students)}')

print(f'Total courses: {total_courses}')
print(f'Total students: {total_students}')