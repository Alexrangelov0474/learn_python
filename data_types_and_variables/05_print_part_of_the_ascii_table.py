starting = int(input())
ending = int(input())

for char in range(starting, ending + 1):
    if char == ending:
        print(chr(char))
    else:
        print(chr(char), end=" ")
