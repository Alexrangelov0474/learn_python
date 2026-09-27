user_points = {}
submissions = {}
while True:
    current_submission = input().split('-')
    if len(current_submission) == 1:
        break
    elif len(current_submission) == 2:
        name = current_submission[0]
        del user_points[name]
    else:
        name, course, points = current_submission[0], current_submission[1], int(current_submission[2])
        if name not in user_points.keys():
            user_points[name] = 0
        if points > user_points[name]:
            user_points[name] = points
        if course not in submissions.keys():
            submissions[course] = 0
        submissions[course] += 1
print('Results:')
for name, points in user_points.items():
    print(f'{name} | {points}')
print('Submissions:')
for course, number_of_submissions in submissions.items():
    print(f'{course} - {number_of_submissions}')