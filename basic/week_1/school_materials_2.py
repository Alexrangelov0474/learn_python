number_pens = int(input())
number_markers = int(input())
litres = int(input())
discount =  int(input())

pen_price = 5.80
marker_price = 7.20
cleaner_price = 1.20

total_price = (number_pens * pen_price) + (number_markers * marker_price) + (litres * cleaner_price)

discount_price = discount / 100 * total_price
final_price = total_price - discount_price

print(final_price)
