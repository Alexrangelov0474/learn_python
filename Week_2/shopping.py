budget = float(input())
gpu = int(input())
cpu = int(input())
ram = float(input())

gpu_price = 250.00
total_gpu_price = gpu_price * gpu

cpu_price = total_gpu_price * 0.35
total_cpu_price = cpu_price * cpu

ram_price = total_gpu_price * 0.10
total_ram_price = ram_price * ram

total_price = total_gpu_price + total_ram_price +total_cpu_price

diff = abs(total_gpu_price - budget)

if gpu > cpu:
    total_price *= 0.85

diff = abs(total_price - budget)

if budget >= total_price:
    print(f'You have {diff:.2f} euro left!')

else:
    print(f'Not enough money! You need {diff:.2f} euro more!')

