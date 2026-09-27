text = input()

sorted_text = [character for character in text if character.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_text))