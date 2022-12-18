from collections import defaultdict, deque
from math import inf
import json

class Grid:
    def __init__(self):
        self.grid = defaultdict(lambda: defaultdict(lambda: '.'))
        self.r_min = 0
        self.r_max = -inf
        self.c_min = inf
        self.c_max = -inf

    def __repr__(self):
        return json.dumps(self.grid)

    def print(self):
        print([c for c in range(self.c_min, self.c_max + 1)])
        for r in range(self.r_min, self.r_max + 1):
            print([self.grid[c][r] for c in range(self.c_min, self.c_max + 1)])

    def build(self, lines):
        "We use a defaultdict so it will automatically populate empty space when calculating the sand drop"

        for line in lines:
            queue = deque()
            for coordinate in line:
                queue.append(tuple([int(x) for x in coordinate.split(',')]))

            previous_coordinate = queue.pop()
            while len(queue):
                next_coordinate = queue.pop()
                self.add_wall(previous_coordinate, next_coordinate)
                previous_coordinate = next_coordinate

    def add_wall(self, c1, c2):
        if (c2[0] != c1[0]):
            for c in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
                self.grid[c][c1[1]] = '#'
        elif (c2[1] != c1[1]):
            for r in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
                self.grid[c1[0]][r] = '#'
        self.r_min = min(self.r_min, c1[1], c2[1])
        self.r_max = max(self.r_max, c1[1], c2[1])
        self.c_min = min(self.c_min, c1[0], c2[0])
        self.c_max = max(self.c_max, c1[0], c2[0])

    def is_void(self,c, r):
        if c < self.c_min or c > self.c_max:
            return True
        if r < self.r_min or r > self.r_max:
            return True
        return False

    def drop_sand(self, c, r):
        "Drops a unit of sand, returns True if it comes to rest, False if it falls into the void."

        neighbors = [
            (c, r + 1),
            (c - 1, r + 1),
            (c + 1, r + 1)
        ]

        for neighbor in neighbors:
            if self.is_void(neighbor[0], neighbor[1]):
                return False

            neighbor_fill = self.grid[neighbor[0]][neighbor[1]]
            if neighbor_fill == '#':
                continue
            if neighbor_fill == 'o':
                continue
            if neighbor_fill == '.':
                return self.drop_sand(neighbor[0], neighbor[1])

        self.grid[c][r] = 'o'
        return True


with open('input') as file:
    lines = [x.strip('\n').replace(' ', '').split('->') for x in file]
    grid = Grid()
    grid.build(lines)

    sand_count = 0
    while True:
        if grid.drop_sand(500, 0):
            sand_count += 1
        else:
            break

    grid.print()
    print(sand_count)