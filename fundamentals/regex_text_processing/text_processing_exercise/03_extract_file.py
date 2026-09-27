path_to_file = input()
filename_and_extension = path_to_file.split('\\')[-1]
filename,extension = filename_and_extension.split('.')
print(f'File name: {filename}')
print(f'File extension: {extension}')