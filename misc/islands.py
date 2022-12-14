def countIslands(map):
    islandsCount = 0
    memo = {(x, y): 0 for x in range(0, len(map)) for y in range(0, len(map[0]))}

    for x in range(0, len(map)):
        for y in range(0, len(map[x])):
            if not memo[(x, y)]:
                checkCell(map, memo, x, y)
                if (map[x][y]):
                    islandsCount = islandsCount + 1

    print(islandsCount)

def checkCell(map, memo, x, y):
    memo[(x, y)] = 1
    if (map[x][y]):
        for cell in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if cell[0] < 0 or cell[1] < 0 or cell[0] >= len(map) or cell[1] >= len(map[0]):
                continue
            elif not memo[(cell[0], cell[1])]:
                checkCell(map, memo, cell[0], cell[1])

countIslands([
    [1, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
])
countIslands([
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
])
countIslands([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
])