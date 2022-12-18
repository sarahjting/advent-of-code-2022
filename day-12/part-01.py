from math import floor

def get_height(map_grid, coordinates):
    current_position_height = map_grid[coordinates[0]][coordinates[1]]
    if current_position_height == 'S':
        return ord('a')
    if current_position_height == 'E':
        return ord('z')
    return ord(current_position_height)


with open('input') as file:
    map_grid = []
    path_grid = []
    src = None
    dst = None

    for file_line in file:
        file_line = file_line.strip('\n')
        src_index = file_line.find('S')
        dst_index = file_line.find('E')
        if src_index > -1:
            src = (len(map_grid), src_index)
        if dst_index > -1:
            dst = (len(map_grid), dst_index)
        map_grid.append(list(file_line))
        path_grid.append([None for x in range(0, len(file_line))])

    # stack for dfs
    positions_to_visit = [(src, 0)]
    while len(positions_to_visit) > 0:
        current_position, current_path_length = positions_to_visit.pop()
        next_path_length = current_path_length + 1

        neighbors = [
            (current_position[0] - 1, current_position[1]), # up
            (current_position[0], current_position[1] + 1), # right
            (current_position[0] + 1, current_position[1]), # down
            (current_position[0], current_position[1] - 1), # left
        ]

        for next_position in neighbors:
            if next_position[0] < 0 or next_position[0] >= len(path_grid):
                continue
            if next_position[1] < 0 or next_position[1] >= len(path_grid[0]):
                continue
            if get_height(map_grid, current_position) < get_height(map_grid, next_position) - 1:
                continue
            existing_path = path_grid[next_position[0]][next_position[1]]
            if (existing_path is None or existing_path > next_path_length):
                path_grid[next_position[0]][next_position[1]] = next_path_length
                positions_to_visit.append((next_position, next_path_length))

    print(path_grid[dst[0]][dst[1]])
