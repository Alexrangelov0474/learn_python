import re
string = input()
pattern = r'([#@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
pairs = 0
mirror_words = []

for match in re.finditer(pattern, string):
    pairs += 1
    first_word = match.group(2)
    second_word = match.group(3)

    if first_word == second_word[::-1]:
        mirror_words.append(f'{first_word} <=> {second_word}')

if pairs == 0:
    print('No word pairs found!')
else:
    print(f'{pairs} word pairs found!')

if not mirror_words:
    print('No mirror words!')
else:
    print('The mirror words are:')


print(', '.join(mirror_words))