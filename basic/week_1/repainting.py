nylon = 1.50
paint = 14.50
thinner = 5
bags = 0.40

nylon_need = int(input())
paint_need = int(input())
thinner_need = int(input())
work_hours = int(input())

more_nylon = (nylon_need + 2)
more_paint = paint_need + (paint_need * 0.10)

total_materials_price = ((more_nylon * nylon) + (more_paint * paint) + (thinner_need * thinner) + bags)

workers_price = total_materials_price * 0.30
workers_final_price = workers_price * work_hours

final_price = workers_final_price + total_materials_price

print(final_price)

