import re
destinations = input()
valid_destinations = []
pattern = r'([=\/])([A-Z][a-zA-Z]{2,})\1'
for match in re.finditer(pattern,destinations):
    valid_destinations.append(match.group(2))

print(f'Destinations: {", ".join(valid_destinations)}')

travel_points = sum(len(destination) for destination in valid_destinations )
print(f'Travel Points: {travel_points}')
