import sys

number_of_elves = sys.argv[1] if len(sys.argv) > 1 else 3
calories = []

def insert_calories(new_calories):
    index = 0
    for current_calories in calories:
        if current_calories < new_calories:
            calories.insert(index, new_calories)
            return
        index = index + 1

    if len(calories) < number_of_elves:
        calories.append(new_calories)
    elif len(calories) > number_of_elves:
        calories.pop()

with open('input') as file:
    current_calories = 0

    for line in file:
        if line == '\n':
            insert_calories(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)

    print(sum(calories))
