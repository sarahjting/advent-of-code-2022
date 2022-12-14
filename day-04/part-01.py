with open('input') as file:
    count = 0

    for line in file:
        line = line.strip('\n')
        range_1, range_2 = [x.split('-') for x in line.split(',')]
        if (int(range_1[0]) <= int(range_2[0]) and int(range_1[1]) >= int(range_2[1])):
            count = count + 1
        elif (int(range_2[0]) <= int(range_1[0]) and int(range_2[1]) >= int(range_1[1])):
            count = count + 1

    print(f'count: {count}')
