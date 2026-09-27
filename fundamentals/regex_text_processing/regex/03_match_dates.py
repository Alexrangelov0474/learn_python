import re

dates = input()

patter = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(patter, dates)

for line in result:
    day = line[0]
    month = line[2]
    year = line[3]

    print(f'Day: {day}, Month: {month}, Year: {year}')