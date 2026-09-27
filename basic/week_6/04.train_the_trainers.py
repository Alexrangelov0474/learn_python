n = int(input())

total_sum = 0
count = 0

while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        break

    grade_sum = 0
    for _ in range(n):
        grade = float(input())
        grade_sum += grade

    avg_grade = grade_sum / n
    print(f'{presentation_name} - {avg_grade:.2f}.')

    count += n
    total_sum += grade_sum

final_assessment = total_sum / count
print(f"Student's final assessment is {final_assessment:.2f}.")