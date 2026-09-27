student = input()
total_score = 0
school_class = 1
max_tries = 0

while True:
    grade = float(input())
    if grade < 4.00:
        max_tries += 1
        if max_tries > 1:
            print(f'{student} has been excluded at {school_class} grade')
            break
        continue
    total_score += grade

    if school_class == 12:
        avg_score = total_score / 12
        print(f'{student} graduated. Average grade: {avg_score:.2f}')
        break
    school_class += 1