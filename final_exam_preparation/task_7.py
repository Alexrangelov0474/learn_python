import re
string = input()

pattern_numbers = r'\d'
threshold = 1
for number in re.finditer(pattern_numbers, string):
    threshold *= int(number.group())

pattern_emoji = r'([:*])\1([A-Z][A-Za-z]{2,})\1\1'
cool_emojies = []
emojies_found_counter = 0
print(f'Cool threshold: {threshold}')
for match in re.finditer(pattern_emoji, string):
    emojies_found_counter += 1
    full_word = match.group()
    word = match.group(2)
    emoji_sum = 0
    for letter in word:
        emoji_sum += ord(letter)
    if emoji_sum >= threshold:
        cool_emojies.append(full_word)

print(f'{emojies_found_counter} emojis found in the text. The cool ones are:')
print('\n '.join(cool_emojies ))

