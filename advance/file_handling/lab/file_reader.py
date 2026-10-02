import os.path
from constants import path_to_dir

path = os.path.join(path_to_dir, 'files', 'numbers.txt')

file = open(path)
numbers = map(int, file.read().split('\n'))
# numbers = [int(el) for el in file.read().split('\n')]
print(sum(numbers))