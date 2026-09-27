def fill_the_box(*args):
    box_size = args[0] * args[1] * args[2]
    boxes_to_add = 0
    for box in args[3:]:
        if box == 'Finish':
            break

        boxes_to_add += int(box)

    if box_size < boxes_to_add:
        return f'No more free space! You have {boxes_to_add - box_size} more cubes.'
    else:
        return f'There is free space in the box. You could put {box_size - boxes_to_add} more cubes.'



print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
