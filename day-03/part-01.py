def item_type_priority(item_type):
    item_type_ord = ord(item_type)
    return item_type_ord - 96 if item_type_ord >= 97 else item_type_ord - 38

with open('input') as file:
    priorities = 0

    for line in file:
        line = line.strip('\n')
        line_length = int(len(line) / 2)
        item_type_intersection = set(line[:line_length]) & set(line[line_length:])
        item_type = item_type_intersection.pop()
        priorities = priorities + item_type_priority(item_type)

    print(f'priorities: {priorities}')
