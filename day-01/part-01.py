with open('input') as file:
    max_calories = 0
    current_calories = 0

    for line in file:
        if line == '\n':
            if (current_calories > max_calories):
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(line)

    print(f'most calories: {max_calories}')
