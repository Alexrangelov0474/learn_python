import re

def check_valid_barcode(barcode:str) -> str:
    pattern = '^@#+(.*)@#+$'
    match_barcode = re.search(pattern, barcode)
    if not match_barcode:
        return 'Invalid barcode'

    found_barcode = match_barcode.group(1)

    if len(found_barcode) < 6:
        return 'Invalid barcode'

    elif (not found_barcode[0].isupper()
          or not found_barcode[0].isupper()):
        return 'Invalid barcode'

    elif not found_barcode.isalnum():
        return 'Invalid barcode'
    product_group = ''
    for symbol in found_barcode:
        if symbol.isdigit():
            product_group += symbol
    if not product_group:
        product_group = '00'
    return f'Product group: {product_group}'

count_of_barcods = int(input())
for some_barcode in range(count_of_barcods):
    current_barcode = input()
    message = check_valid_barcode(current_barcode)
    print(message)
