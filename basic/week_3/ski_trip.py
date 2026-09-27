days = int(input())
room_type = input()
rating = input()

nights = days - 1
room_for_one_person_price = 0
apartment_price = 0
president_apartment_price = 0

if room_type == 'room for one person':
    room_for_one_person_price = nights * 18
    if rating == 'positive':
        room_for_one_person_price *= 1.25
    elif rating == 'negative':
        room_for_one_person_price *= 1.25
    print(f'{room_for_one_person_price:.2f}')

elif room_type == 'apartment':
    apartment_price = nights * 25
    if nights < 10:
        apartment_price *= 0.70
    elif 10 <= nights <= 15:
        apartment_price *= 0.65
    else:
        apartment_price *= 0.50
    if rating == 'positive':
        apartment_price *= 1.25
    elif rating == 'negative':
        apartment_price *= 0.90
    print(f'{apartment_price:.2f}')

elif room_type == 'president apartment':
    president_apartment_price = nights * 35
    if nights < 10:
        president_apartment_price *= 0.90
    elif 10 <= nights <= 15:
        president_apartment_price *= 0.85
    else:
        president_apartment_price *= 0.80
    if rating == 'positive':
        president_apartment_price *= 1.25
    elif rating == 'negative':
        president_apartment_price *= 0.90
    print(f'{president_apartment_price:.2f}')

