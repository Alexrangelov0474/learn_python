import re
telephones = input()

patter = r'\+359-2-\d{3}\b-\d{4}\b|\+359 2 \d{3}\b \d{4}\b'

result =re.findall(patter, telephones)
print(', '.join(result))
