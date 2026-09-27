bad_grades = int(input())

total_grades = 0
last_exam_name = ''
total_exams = 0
bad_grade_count = 0

while True:
    exam_name = input()

    if exam_name == 'Enough':
        avg_score = total_grades / total_exams
        print(f'Average score: {avg_score:.2f}\n'
              f'Number of problems: {total_exams}\n'
              f'Last problem: {last_exam_name}')
        break

    grade = int(input())
    total_grades += grade
    total_exams += 1
    last_exam_name = exam_name

    if grade <= 4:
        bad_grade_count += 1

        if bad_grade_count == bad_grades:
            print(f"You need a break, {bad_grade_count} poor grades.")
            break





