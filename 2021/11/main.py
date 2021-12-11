from dataclasses import dataclass
from functools import reduce


@dataclass(frozen=True, eq=True)
class Point:
    i: str
    x: int
    y: int


def get_adjacent_points(x, y, grid):
    adj = []
    for y_i in range(y-1, y+2):
        adj += list(filter(lambda a: not (a.i is None), [Point(grid[y_i][i], i, y_i) for i in range(x-1, x+2)]))
    return adj


def print_grid(grid):
    for y in range(1, len(grid)-1):
        print(''.join([str(grid[y][x]) for x in range(1, len(grid[0])-1)]))


def search(x, y, grid):
    if grid[y][x] > 9:
        # print(f"Flashed {(x-1, y-1)}")
        grid[y][x] = -1
        for adj in get_adjacent_points(x, y, grid):
            if grid[adj.y][adj.x] >= 0:
                grid[adj.y][adj.x] += 1
                search(adj.x, adj.y, grid)


if __name__ == '__main__':
    grid = []
    with open('input') as f:
        for line in f:
            grid.append([None] + list(map(int, line.strip())) + [None])

    grid.insert(0, [None] * len(grid[0]))
    grid.append([None] * len(grid[0]))

    print("Before")
    print_grid(grid)

    flashed = 0
    for step in range(100):
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[0]) - 1):
                grid[y][x] += 1

        while True:
            for y in range(1, len(grid)-1):
                for x in range(1, len(grid[0])-1):
                    p = grid[y][x]
                    if p > 9:
                        search(x, y, grid)
            if 10 not in reduce(lambda l, s: s + l, grid):
                break

        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[0]) - 1):
                if grid[y][x] < 0:
                    flashed += 1
                    grid[y][x] = max(0, grid[y][x])

        print(f"After step {step+1}")
        print_grid(grid)

    print(flashed)
