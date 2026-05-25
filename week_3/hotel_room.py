month = input()
number_of_nights = int(input())

apartment_price = 0
studio_price = 0

if month == 'May' or month == 'October':
    studio_price = number_of_nights * 50
    apartment_price = number_of_nights * 65
elif month == 'June' or month == 'September':
    studio_price = number_of_nights * 75.20
    apartment_price = number_of_nights * 68.70
elif month == 'July' or month == 'August':
    studio_price = number_of_nights * 76
    apartment_price =number_of_nights * 77

if 7 < number_of_nights <= 14 and (month == 'May' or month == 'October'):
    studio_price *= 0.95
elif number_of_nights > 14 and (month == 'May' or month == 'October'):
    studio_price *= 0.70
elif number_of_nights > 14 and (month == 'June' or month == 'September'):
    studio_price *= 0.80
if number_of_nights > 14:
    apartment_price *= 0.90

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')

