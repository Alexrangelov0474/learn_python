def create_sequence(n:int):
    seq = [0, 1]

    for num in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(num:int, seq:list):
    try:
        index = seq.index(num)
        return f"The number - {num} is at index {index}"
    except ValueError:
        return f"The number {num} is not in the sequence"

