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


if __name__ == '__main__':
    with open('input') as f:
        grid = [list(map(int, l.strip())) for l in f]

        dist = {}
        q = heapdict()
        prev = {}
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                p = Point(grid[y][x], x, y)
                dist[p] = math.inf
                q[p] = math.inf
                prev[p] = None

        dist[Point(grid[0][0], 0, 0)] = 0

        print(grid)
        print(get_adjacent_points(Point(grid[0][0], 0, 0), grid))

        while q:
            u, p = q.popitem()
            print(u)
            for a in get_adjacent_points(u, grid):
                t = a.i + dist[u]
                if t < dist[a]:
                    dist[a] = t
                    prev[a] = u
                    q[a] = t

        x = len(grid[0]) - 1
        y = len(grid) - 1
        print(dist[Point(grid[y][x], x, y)])
