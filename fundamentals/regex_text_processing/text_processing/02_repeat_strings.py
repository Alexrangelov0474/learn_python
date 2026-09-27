string = input().split()
new_text = [text * len(text) for text in string]
print(''.join(new_text))