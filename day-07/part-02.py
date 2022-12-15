dir_to_parents = {'': []}
dir_sizes = {'': 0}

with open('input') as file:
    current_dir = None
    for line in file:
        line = line.strip('\n')

        if line[0:6] == '$ cd /':
            current_dir = ''
        elif line[0:7] == '$ cd ..':
            current_dir = dir_to_parents[current_dir][0]
        elif line[0:5] == '$ cd ':
            current_dir = current_dir + '/' + line[5:]
        elif line == '$ ls':
            pass
        elif line[0:4] == 'dir ':
            dir_sizes[current_dir + '/' + line[4:]] = 0
            dir_to_parents[current_dir + '/' + line[4:]] = [current_dir] + dir_to_parents[current_dir]
        else:
            size, file_name = line.split(' ')
            if not size.isnumeric():
                print('Invalid size provided')
            else:
                size = int(size)
                dir_sizes[current_dir] += size
                for dir in dir_to_parents[current_dir]:
                    dir_sizes[dir] += size

    space_required = dir_sizes[''] - 40000000
    print(min([size for (dir, size) in dir_sizes.items() if size >= space_required]))
