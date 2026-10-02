import os.path
from constants import path_to_dir

path = os.path.join(path_to_dir, 'files')

with open(os.path.join(path, "my_first_file.txt"), 'w') as file:
    file.write('I just created my first file!')