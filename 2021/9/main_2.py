def get_adjacent_points(x, y, height_map):
    w_y = [(height_map[i][x], x, i) for i in range(y-1, y+2)]
    w_x = [(height_map[y][i], i, y) for i in range(x-1, x+2)]
    w_y.pop(1)
    w_x.pop(1)
    return w_x, w_y


def search_basin(x, y, height_map):
    p = height_map[y][x]
    if p == 9:
        return 0
    else:
        t = 0
        adj_x, adj_y = get_adjacent_points(x, y, height_map)
        for adj in adj_x:
            t += search_basin(adj[1], adj[2], height_map)
        for adj in adj_y:
            t += search_basin(adj[1], adj[2], height_map)
        return t


if __name__ == '__main__':
    with open('test_input') as f:
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
                if w_x[0][0] > line[x] < w_x[1][0] and w_y[0][0] > line[x] < w_y[1][0]:
                    t += int(line[x]) + 1
                    low_points.append((line[x], x, y))

        print(t)
        print(low_points)

        print(search_basin(low_points[0][1], low_points[0][2], height_map))