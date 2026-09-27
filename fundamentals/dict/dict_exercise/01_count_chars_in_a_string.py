characters = input()
occurrences = {}
for char in characters:
    if char == ' ':
        continue
    if char not in occurrences.keys():
        occurrences[char] = 0
    occurrences[char] += 1

for character, repetitions in occurrences.items():
    print(f"{character} -> {repetitions}")