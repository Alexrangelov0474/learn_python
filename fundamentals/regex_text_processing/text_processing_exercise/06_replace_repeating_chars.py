text = input()
final_text = ''
for character in text:
    if not final_text or character != final_text[-1]:
        final_text += character
print(final_text)