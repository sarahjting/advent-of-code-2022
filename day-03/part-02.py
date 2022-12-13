def item_type_priority(item_type):
    item_type_ord = ord(item_type)
    return item_type_ord - 96 if item_type_ord >= 97 else item_type_ord - 38

with open('input') as file:
    priorities = 0

    current_elf_counter = 0
    current_priority = 0
    current_rucksacks = []

    for line in file:
        current_rucksacks.append(set(line.strip('\n')))
        current_elf_counter = current_elf_counter + 1
        if (current_elf_counter == 3):
            item_type_intersection = current_rucksacks[0] & current_rucksacks[1] & current_rucksacks[2]
            item_type = item_type_intersection.pop()
            priorities = priorities + item_type_priority(item_type)
            current_elf_counter = 0
            current_rucksacks = []

    print(f'priorities: {priorities}')
