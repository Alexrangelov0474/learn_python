import re

pattern = r'(w{3}\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'
sentence = input()
while sentence:
    match = re.search(pattern, sentence)
    if match:
        link = match.group(1)
        print(link)

    sentence = input()

