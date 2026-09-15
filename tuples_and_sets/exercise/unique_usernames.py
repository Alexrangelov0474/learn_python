# number_of_lines = int(input())

names = set()
for _ in range(int(input())):
    names.add(input())

print(*names, sep='\n')

# for name in names:
#     print(name)

