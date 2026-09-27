prime_num = 0
non_prime_num = 0
command = input()
while command !='stop':
    num = int(command)
    if num < 0:
        print(f'Number is negative.')
        command = input()
        continue

    is_prime = True
    if num == 0 or num == 1:
        is_prime = False
    else:
        for dij in range(2, num):
            if num % dij == 0:
                is_prime = False
                break

    if is_prime:
        prime_num += num
    else:
        non_prime_num += num
    command = input()

print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime_num}")

