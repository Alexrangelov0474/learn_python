actor_name = input()
academy_points = float(input())
n_teachers = int(input())

total_points = academy_points
points_needed = 1250.5

for _ in range(n_teachers):
    teacher_name = input()
    points = float(input())

    total_points += (len(teacher_name) * points) / 2

    if total_points > points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    diff = abs(total_points - points_needed)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")


