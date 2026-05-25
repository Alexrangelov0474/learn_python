#	Пакет химикали - 5.80 лв.
#	Пакет маркери - 7.20 лв.
#	Препарат - 1.20 лв (за литър)

#	Брой пакети химикали - цяло число в интервала [0...100]
#	Брой пакети маркери - цяло число в интервала [0...100]
#	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#	Процент намаление - цяло число в интервала [0...100]

number_pens = int(input(f'How many pens? ' ))
number_markers = int(input(f'How many markers? ' ))
litres = int(input(f'How many litres? ' ))
discount = int(input(f'How much discounts? ' ))

price_board_cleaner = litres * 1.20
price_pens = number_pens * 5.80
price_markers = number_markers * 7.20
total_price = price_pens + price_markers + price_board_cleaner
final_discount = total_price - ((discount / 100) * total_price)


print (f'price for pens: {price_pens}')
print (f'price for markers: {price_markers}')
print (f'price for board cleaner: {price_board_cleaner}')
print (f'total price: {total_price}')
print (f'the price with discount is: {final_discount}')

answer = str(input(f'Only for you we have more discount for 10%. Do you want it? Yes or No?: ')) .lower()
more_discount = final_discount - (final_discount * 0.10)

if answer == 'yes':
    print(f'your more discount is {more_discount}')
else:
    print(f'okay nevermind!')


