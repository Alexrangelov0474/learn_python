def loading_bar_function(percents: int) -> str:
    if percents == 100:
        return ("100% Complete!\n[%%%%%%%%%%]")
    percents_loaded = percents // 10
    not_loaded_percents = 10 - percents_loaded
    return f'{percents}% [' \
           f'{"%" * percents_loaded}' \
           f'{"." * not_loaded_percents}' \
           f']\nStill loading...'



number_as_integer = int(input())
print(loading_bar_function(number_as_integer))