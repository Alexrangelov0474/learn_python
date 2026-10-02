import os.path
from constants import path_to_dir

path = os.path.join(path_to_dir, 'files','file_to_delete.txt')

try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted!')