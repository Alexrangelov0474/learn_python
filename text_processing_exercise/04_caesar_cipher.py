message = input()
encrypted_message = ''
for text in message:
    encrypted_char = chr(ord(text) + 3)
    encrypted_message += encrypted_char
print(encrypted_message)