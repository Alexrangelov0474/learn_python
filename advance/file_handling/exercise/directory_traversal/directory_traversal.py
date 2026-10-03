import os

files = {}
directory = '../'

def get_file(folder, level = float('inf')):
    if level < 0:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)

        if os.path.isfile(f):
            _, extension = os.path.splitext(element)
            if extension:
                if extension not in files:
                    files[extension] = []
                files[extension].append(element)

        elif os.path.isdir(f):
            get_file(f, level - 1)

get_file(directory)

with open(os.path.join(directory, 'report.txt'), 'w') as output:
    for extension, filename in sorted(files.items()):
        output.write(f'{extension}\n')
        for f_name in sorted(filename):
            output.write(f'- - - {f_name}\n')
