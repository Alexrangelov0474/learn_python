def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'odd':
            kwargs[key] = list(filter(lambda x: x % 2 != 0, value))
        else:
            kwargs[key] = list(filter(lambda x: x % 2 == 0, value))

    sorted_dict = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
    return dict(sorted_dict)

print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))