steps_goal = 10000
total_steps = 0
command = input()
diff = 0

while command != 'Going home':
    command = int(command)
    total_steps += command
    diff = abs(total_steps - steps_goal)
    if total_steps >= steps_goal:
        print(f'Goal reached! Good job!\n {diff} steps over the goal!')
        break

    command = input()

if command == 'Going home':
    steps_home = int(input())
    total_steps += steps_home
    diff = abs(total_steps - steps_goal)
    if total_steps >= steps_goal:
        print(f'Goal reached! Good job!\n {diff} steps over the goal!')
    else:
        print(f"{diff} more steps to reach goal.")
