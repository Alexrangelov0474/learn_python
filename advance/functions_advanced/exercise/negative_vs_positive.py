def print_biggest(p_sum: int, n_sum: int) -> str:
    if abs(n_sum) > p_sum:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


def sum_nums(*args: int) -> tuple:
    p_sum = 0
    n_sum = 0

    for num in args:
        if num > 0:
            p_sum += num
        else:
            n_sum += num
    return p_sum, n_sum

numbers = map(int, input().split())
pos_sum, neg_sum = sum_nums(*numbers)

print(neg_sum)
print(pos_sum)
print(print_biggest(pos_sum, neg_sum))


