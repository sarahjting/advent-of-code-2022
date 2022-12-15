def find_start_of_packet(string):
    index = 4
    last_four = line[0:4]
    while (index <= len(line)):
        if len(set(last_four)) == 4:
            return index

        index += 1
        last_four = line[index-4:index]


with open('input') as file:
    for line in file:
        print(find_start_of_packet(line.strip('\n')))