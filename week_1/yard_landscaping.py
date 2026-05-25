print (f'how much square metres for landscape?')
square_metres_for_landscaped = float(input())
the_final_price = square_metres_for_landscaped * 7.61
the_discount_price = the_final_price * 0.18

print(f'the final price is: {the_final_price}')
print(f'the discount price is: {the_discount_price}')

print(f'Are you good with the price?')
mood = str(input()).lower()
if mood == 'yes':
 print (f'Im happy with that.')
else:
 print (f'im sorry for that')
