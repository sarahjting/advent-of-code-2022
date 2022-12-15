marker_characters = 14

def find_start_of_packet(string):
    index = marker_characters
    last_four = line[0:marker_characters]
    while (index <= len(line)):
        if len(set(last_four)) == marker_characters:
            return index

        index += 1
        last_four = line[index-marker_characters:index]


with open('input') as file:
    for line in file:
        print(find_start_of_packet(line.strip('\n')))