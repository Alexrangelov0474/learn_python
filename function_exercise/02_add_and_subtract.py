def sum_numbers(num_1,num_2):
    return num_1 + num_2

def subtract(sum_result,num_3):
    return sum_result - num_3

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

sum_result = sum_numbers(num_1,num_2)
subtract_result = subtract(sum_result, num_3)

print(subtract_result)