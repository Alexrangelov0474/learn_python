elements = input().split()
moves = 0
command = input()

while command != "end":
    moves += 1
    first, second = map(int, command.split())

    if first == second:
        middle = len(elements) // 2

        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")

    command = input()
print(elements)