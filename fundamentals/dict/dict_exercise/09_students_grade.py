results = {}
number_of_lines = int(input())

for row in range(number_of_lines):
    student_name = input()
    grade = float(input())
    if student_name not in results:
        results[student_name] = []
    results[student_name].append(grade)

for student_name, grades in results.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
       print(f'{student_name} -> {avg_grade:.2f}')
