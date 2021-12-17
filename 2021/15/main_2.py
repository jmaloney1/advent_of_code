import math
from dataclasses import dataclass

from heapdict import heapdict


@dataclass(frozen=True, eq=True, order=True)
class Point:
    i: int
    x: int
    y: int


def get_adjacent_points(p, grid):
    adj = set()
    x = p.x
    y = p.y
    if x != 0:
        adj.add(Point(grid[y][x - 1], x - 1, y))
    if x != len(grid[0]) - 1:
        adj.add(Point(grid[y][x + 1], x + 1, y))
    if y != 0:
        adj.add(Point(grid[y - 1][x], x, y - 1))
    if y != len(grid) - 1:
        adj.add(Point(grid[y + 1][x], x, y + 1))

    return adj


def print_grid(grid):
    for y in range(len(grid)):
        print(''.join(map(str, grid[y])))


if __name__ == '__main__':
    with open('input') as f:
        grid = [list(map(int, l.strip())) for l in f]

        full_grid = [[0] * len(grid[0]) * 5 for _ in range(len(grid) * 5)]
        for y_i in range(0, 5):
            for x_i in range(0, 5):
                for y in range(len(grid)):
                    for x in range(len(grid[0])):
                        c = grid[y][x] + y_i + x_i
                        if c > 9:
                            c += 1
                        full_grid[y_i * len(grid) + y][x_i * len(grid[0]) + x] = c % 10

        dist = {}
        q = heapdict()
        prev = {}
        for y in range(len(full_grid)):
            for x in range(len(full_grid[0])):
                p = Point(full_grid[y][x], x, y)
                dist[p] = math.inf
                q[p] = math.inf
                prev[p] = None

        dist[Point(full_grid[0][0], 0, 0)] = 0

        # print_grid(full_grid)

        while q:
            u, p = q.popitem()
            for a in get_adjacent_points(u, full_grid):
                t = a.i + dist[u]
                if t < dist[a]:
                    dist[a] = t
                    prev[a] = u
                    q[a] = t

        x = len(full_grid[0]) - 1
        y = len(full_grid) - 1
        print(dist[Point(full_grid[y][x], x, y)])
