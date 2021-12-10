from dataclasses import dataclass
from functools import reduce


@dataclass(frozen=True, eq=True)
class Point:
    i: str
    x: int
    y: int


def get_adjacent_points(x, y, height_map):
    w_y = [Point(height_map[i][x], x, i) for i in range(y-1, y+2)]
    w_x = [Point(height_map[y][i], i, y) for i in range(x-1, x+2)]
    w_y.pop(1)
    w_x.pop(1)
    return w_x, w_y


def search_basin(p, height_map, n):
    if p.i == '9' or p in n:
        return {}
    else:
        adj_x, adj_y = get_adjacent_points(p.x, p.y, height_map)
        n = n.union({p})
        for adj in adj_x + adj_y:
            n = n.union(search_basin(adj, height_map, n))
        return n


if __name__ == '__main__':
    with open('input') as f:
        height_map = ['9' + l.strip() + '9' for l in f]

        # wrap in 9s
        height_map.insert(0, '9' * len(height_map[0]))
        height_map.append('9' * len(height_map[0]))

        t = 0
        low_points = []
        for y in range(1, len(height_map)-1):
            line = height_map[y]
            for x in range(1, len(line)-1):
                w_x, w_y = get_adjacent_points(x, y, height_map)
                if w_x[0].i > line[x] < w_x[1].i and w_y[0].i > line[x] < w_y[1].i:
                    t += int(line[x]) + 1
                    low_points.append(Point(line[x], x, y))

        basins = []
        for l in low_points:
            basin = search_basin(l, height_map, set())
            print(basin)
            basins.append(basin)

        print(reduce(lambda x, s: x * s, sorted(map(len, basins))[-3:]))
