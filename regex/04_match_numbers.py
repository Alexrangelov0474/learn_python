import re

numbers = input()

patter = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(patter,numbers)
for match in result:
    print(match.group(), end=' ')

