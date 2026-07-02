students_activity = {}
while True:
    line = input()
    if line == 'finish':
        break
    student,subject = line.split()

    if student not in students_activity:
        students_activity[student] = []
        students_activity[student].append(subject)
    else:
        students_activity[student].append(subject)

total_students = len(students_activity)
print('Students:')
for student, subjects in students_activity.items():
    subject_str = ', '.join(subjects)
    print(f'{student}-> {subject_str}')
print(f'Total students: {total_students}')