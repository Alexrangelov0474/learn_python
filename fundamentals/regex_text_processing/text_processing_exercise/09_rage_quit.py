text = input()
sub_text = ''
rage_message = ''
repetitions = ''
for index in range(len(text)):
    if not text[index].isdigit():
        sub_text += text[index].upper()
    else:
        repetitions += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetitions += text[index +1]
        rage_message += sub_text * int(repetitions)
        sub_text = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)