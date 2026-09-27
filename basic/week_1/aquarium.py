#.	Дължина в см – цяло число в интервала [10 … 500]
#.	Широчина в см – цяло число в интервала [10 … 300]
#.	Височина в см – цяло число в интервала [10… 200]
#.	Процент  – реално число в интервала [0.000 … 100.000]

length = int(input())
width = int(input())
height = int(input())
percent =float(input())

volume_cm3 = length * width * height
volume_litres = volume_cm3 / 1000

occupied_space = percent / 100
needed_litres = volume_litres * (1-occupied_space)

print(needed_litres)
print(f'Браво бе маняк!!!')