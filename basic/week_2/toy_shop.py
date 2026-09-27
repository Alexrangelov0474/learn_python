#	Пъзел - 2.60 лв.
#	Говореща кукла - 3 лв.
#	Плюшено мече - 4.10 лв.
#	Миньон - 8.20 лв.
#	Камионче - 2 лв.
from ipaddress import v4_int_to_packed

#.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
#.	Брой пъзели - цяло число в интервала [0… 1000]
#.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
#	Брой плюшени мечета - цяло число в интервала [0 … 1000]
#.	Брой миньони - цяло число в интервала [0 … 1000]
#	Брой камиончета - цяло число в интервала [0 … 1000]

puzzle = 2.60
talking_dool = 3.00
bear = 4.10
minion = 8.20
truck = 2.00
discount = 0

vacation_prize = float(input())
amount_puzzle = int(input())
amount_talking_dool = int(input())
amount_bear = int(input())
amount_minion = int(input())
amount_truck = int(input())

order_amount = ((amount_puzzle *puzzle)
                + (amount_talking_dool * talking_dool)
                + (amount_bear * bear)
                + (amount_minion * minion)
                + (amount_truck * truck))

total_toys = amount_puzzle + amount_talking_dool + amount_bear + amount_minion + amount_truck

if total_toys >= 50:
    order_amount *= 0.75

rent = order_amount * 0.10
profit = order_amount - rent

difference = abs(profit - vacation_prize)

if profit >= vacation_prize:
    print(f'Yes!{difference:.2f} euro left')
else:
    print(f'Not enough money! {difference:.2f} euro needed')




