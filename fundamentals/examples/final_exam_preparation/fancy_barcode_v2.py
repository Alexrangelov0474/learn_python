import re

pattern = '^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$'

count_of_barcodes = int(input())
for some_barcode in range(count_of_barcodes):
    product_group = ''
    current_barcode = input()
    validator = re.search(pattern,current_barcode)
    if validator:
        for symbol in validator.group(1):
            if symbol.isdigit():
                product_group += symbol
        if not product_group:
            product_group = '00'

        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
